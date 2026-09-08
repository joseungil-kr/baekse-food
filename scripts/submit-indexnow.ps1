param(
    [string]$Url = ""
)

$HostName = "baeksefood.com"
$Key = "baekse9f82d44c80b572a1e038f87e21"
$KeyLocation = "https://$HostName/$Key.txt"
$Endpoint = "https://api.indexnow.org/indexnow"

$UrlList = @()

if ($Url -ne "") {
    $UrlList += $Url
} else {
    $SitemapPath = Join-Path $PSScriptRoot "..\public\sitemap.xml"
    if (-not (Test-Path $SitemapPath)) {
        Write-Host "public/sitemap.xml not found. Running hugo --minify..." -ForegroundColor Yellow
        Push-Location (Join-Path $PSScriptRoot "..")
        hugo --minify
        Pop-Location
    }

    if (Test-Path $SitemapPath) {
        [xml]$xml = Get-Content $SitemapPath -Raw -Encoding UTF8
        if ($xml.sitemapindex) {
            foreach ($sm in $xml.sitemapindex.sitemap) {
                $rel = $sm.loc.Replace("https://$HostName/", "").TrimStart("/")
                $subFile = Join-Path $PSScriptRoot "..\public\$rel"
                if (Test-Path $subFile) {
                    [xml]$subXml = Get-Content $subFile -Raw -Encoding UTF8
                    if ($subXml.urlset -and $subXml.urlset.url) {
                        $UrlList += @($subXml.urlset.url.loc)
                    }
                }
            }
        } elseif ($xml.urlset) {
            $UrlList = @($xml.urlset.url.loc)
        }
    }
}

if ($UrlList.Count -eq 0) {
    Write-Host "No URLs to submit." -ForegroundColor Red
    exit 1
}

$UrlList = @($UrlList | Select-Object -Unique)

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  Baekse Food IndexNow URL Submission (Multilingual)" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "Host: $HostName"
Write-Host "Key Location: $KeyLocation"
Write-Host "Target URLs Count: $($UrlList.Count)"
Write-Host ""

$PayloadObj = @{
    host = $HostName
    key = $Key
    keyLocation = $KeyLocation
    urlList = $UrlList
}

$JsonBody = $PayloadObj | ConvertTo-Json -Depth 5

try {
    $response = Invoke-RestMethod -Uri $Endpoint -Method Post -Body $JsonBody -ContentType "application/json; charset=utf-8"
    Write-Host "IndexNow submission succeeded! (HTTP 200 OK)" -ForegroundColor Green
    Write-Host "$($UrlList.Count) multilingual URLs have been sent to search engines (Naver, Bing, Yandex, etc.)." -ForegroundColor Green
} catch {
    $code = $_.Exception.Response.StatusCode.value__
    if ($code -eq 200 -or $code -eq 202) {
        Write-Host "IndexNow request accepted! (HTTP $code Accepted)" -ForegroundColor Green
        Write-Host "$($UrlList.Count) multilingual URLs received and scheduled for crawling." -ForegroundColor Green
    } else {
        Write-Host "Status Code: $code" -ForegroundColor Yellow
        Write-Host "Error: $($_.Exception.Message)" -ForegroundColor Red
    }
}
