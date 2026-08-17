(function () {
  var dailyInput = document.getElementById('calc-daily');
  if (!dailyInput) return;

  var RENT = { 15: 250, 20: 320, 30: 450 };
  var LABOR = { 15: 420, 20: 560, 30: 820 };
  var pyeong = 20, daily = 180;

  function fmt(n) { return n.toLocaleString('ko-KR'); }
  function set(id, text) { var el = document.getElementById(id); if (el) el.textContent = text; }

  function render() {
    var sales = daily * 30;
    var food = Math.round(sales * 0.32);
    var util = Math.round(sales * 0.05);
    var rent = RENT[pyeong];
    var labor = LABOR[pyeong];
    var net = Math.max(0, sales - food - util - rent - labor);
    set('calc-daily-label', fmt(daily) + '만 원');
    set('calc-sales', fmt(sales) + '만원');
    set('calc-food', '− ' + fmt(food) + '만원');
    set('calc-rent', '− ' + fmt(rent) + '만원');
    set('calc-labor', '− ' + fmt(labor) + '만원');
    set('calc-util', '− ' + fmt(util) + '만원');
    set('calc-net', fmt(net));
    set('calc-summary', pyeong + '평 · 일매출 ' + fmt(daily) + '만 원 기준');
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
