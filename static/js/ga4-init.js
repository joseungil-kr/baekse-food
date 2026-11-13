(() => {
 const id=document.currentScript?.dataset.ga4Id;
 if (!/^G-[A-Z0-9]+$/.test(id||'') || !['baeksefood.com','www.baeksefood.com'].includes(location.hostname)) return;
 window.dataLayer=window.dataLayer||[];
 function gtag(){window.dataLayer.push(arguments);}
 gtag('js',new Date());
 gtag('config',id,{page_location:location.origin+location.pathname});
 const script=document.createElement('script');
 script.async=true;script.src='https://www.googletagmanager.com/gtag/js?id='+id;
 document.head.appendChild(script);
})();
