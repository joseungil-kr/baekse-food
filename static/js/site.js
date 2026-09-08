(function () {
  var dailyInput = document.getElementById('calc-daily');
  if (!dailyInput) return;

  var RENT = { 15: 250, 20: 320, 30: 450 };
  var LABOR = { 15: 420, 20: 560, 30: 820 };
  var pyeong = 20, daily = 180;
  var lang = document.documentElement.lang || 'ko';

  function fmt(n) { return n.toLocaleString('en-US'); }
  function set(id, text) { var el = document.getElementById(id); if (el) el.textContent = text; }

  function formatCurrency(val, spaced) {
    if (lang === 'ko') return fmt(val) + (spaced ? '만 원' : '만원');
    if (lang === 'zh') return fmt(val) + '万韩元';
    if (lang === 'ja') return fmt(val) + '万ウォン';
    var actual = val * 10000;
    return '₩' + fmt(actual);
  }

  function getPyeongText(p) {
    if (lang === 'ko') return p + '평';
    if (lang === 'zh') return p + '坪';
    if (lang === 'ja') return p + '坪';
    if (lang === 'ru') return p + ' пхён';
    return p + ' py';
  }

  function getSummaryText(p, d) {
    var pText = getPyeongText(p);
    var dText = formatCurrency(d, true);
    if (lang === 'en') return 'Based on ' + pText + ' & daily sales of ' + dText;
    if (lang === 'zh') return '以 ' + pText + ' · 日营业额 ' + dText + ' 为基准';
    if (lang === 'ja') return pText + ' · 日商 ' + dText + ' 基準';
    if (lang === 'ru') return 'На основе ' + pText + ' и ежедневных продаж ' + dText;
    return pText + ' · 일매출 ' + dText + ' 기준';
  }

  function render() {
    var sales = daily * 30;
    var food = Math.round(sales * 0.32);
    var util = Math.round(sales * 0.05);
    var rent = RENT[pyeong];
    var labor = LABOR[pyeong];
    var net = Math.max(0, sales - food - util - rent - labor);
    
    set('calc-daily-label', formatCurrency(daily, true));
    set('calc-sales', formatCurrency(sales));
    set('calc-food', '− ' + formatCurrency(food));
    set('calc-rent', '− ' + formatCurrency(rent));
    set('calc-labor', '− ' + formatCurrency(labor));
    set('calc-util', '− ' + formatCurrency(util));
    
    if (lang === 'en' || lang === 'ru') {
      var netActual = net * 10000;
      set('calc-net', '₩' + fmt(netActual));
      set('calc-net-unit', '');
    } else {
      set('calc-net', fmt(net));
      if (lang === 'ko') set('calc-net-unit', '만원');
      else if (lang === 'zh') set('calc-net-unit', '万韩元');
      else if (lang === 'ja') set('calc-net-unit', '万ウォン');
    }
    
    set('calc-summary', getSummaryText(pyeong, daily));
  }

  document.querySelectorAll('#calc-pyeong .chip').forEach(function (btn) {
    btn.addEventListener('click', function () {
      pyeong = Number(btn.dataset.pyeong);
      document.querySelectorAll('#calc-pyeong .chip').forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      render();
    });
  });

  dailyInput.addEventListener('input', function (e) {
    daily = Number(e.target.value);
    render();
  });

  render();
})();
