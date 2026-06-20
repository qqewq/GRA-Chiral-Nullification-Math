# GRA-Chiral-Nullification-Math

**ГРА-хиральность как универсальный язык обнуления симметрии**  
Математический фундамент GRA-экосистемы: оператор обнулёнки = оператор порождения хиральной пары.

## Основная идея

GRA-обнулёнка — это не тривиальное зануление, а **конструктивный переход**  
`(Политика, Веса, Состояние) → (R, L, 0, 0)`,  
где `R` — правая хиральность, `L = Z(R)` — левая (зеркальный образ).  

Эта операция вскрывает фундаментальную связь: **любое обнуление есть акт нарушения зеркальной симметрии**, а хиральность — нативный носитель субъект-инструментной двойственности.

## Структура

- `src/gra_chiral_null/` — чистая математика: хиральность, обнуляющий оператор, эквивалентность.
- `applications/` — революционные расчёты в физике, биологии, химии, лингвистике, экономике, нейронауке, космологии, социальных науках, искусстве и квантовых вычислениях.
- `experiments/` — верификация теории на модельных системах.
- `notebooks/` — интерактивные демонстрации и визуализации.
- `frontend/` — веб-приложение для построения хиральных пар.
- `docs/` — подробное изложение теории.

## Быстрый старт

```bash
git clone https://github.com/qqewq/GRA-Chiral-Nullification-Math
cd GRA-Chiral-Nullification-Math
pip install -r requirements.txt
python -m pytest tests/
streamlit run frontend/app.py
```

## Связь с GRA-экосистемой

Данный репозиторий служит математическим ядром для:

- [GRA-Meta-Nulling-Foundations](https://github.com/qqewq/GRA-Meta-Nulling-Foundations)
- [GRA-SubjectSwap](https://github.com/qqewq/GRA-SubjectSwap)
- [GRA-ASI-Metric-Space](https://github.com/qqewq/GRA-ASI-Metric-Space)
- [GRA-Quantum-Poetry](https://github.com/qqewq/gra-quantum-poetry)

Все они импортируют `gra_chiral_null` как каноническую библиотеку.
