# GRA-Chiral-Nullification-Math  
**ГРА-хиральность как универсальный язык обнуления симметрии**  
**GRA chirality as a universal language of symmetry nullification**

Математическое ядро GRA-экосистемы: оператор обнулёнки = оператор порождения хиральной пары.  
A mathematical core of the GRA ecosystem: the nullification operator = the generator of a chiral pair.

---

## 1. Основная идея / Core idea

**RU**

GRA-обнулёнка — это не тривиальное зануление, а **конструктивный переход**

\[
(\text{Политика}, \text{Веса}, \text{Состояние}) \;\longrightarrow\; (R, L, 0, 0),
\]

где:

- \(R\) — «правая» хиральная конфигурация (исходный объект/политика),
- \(L = Z(R)\) — «левая» конфигурация, образ под зеркальным оператором \(Z\),
- оба собираются в чёткую хиральную пару \((R, L)\),
- все «массы» (weights/state) при этом обнуляются.

Интуитивно: **любое осмысленное обнуление — это акт нарушения зеркальной симметрии**, а хиральность — естественный носитель субъект‑инструментной двойственности (subject/instrument split) в GRA.

---

**EN**

GRA nullification is not a trivial “set everything to zero”, but a **constructive transition**

\[
(\text{Policy}, \text{Weights}, \text{State}) \;\longrightarrow\; (R, L, 0, 0),
\]

where:

- \(R\) is the “right” chiral configuration (the original object/policy),
- \(L = Z(R)\) is the “left” configuration, obtained via a mirror operator \(Z\),
- together they form a well‑defined chiral pair \((R, L)\),
- all “mass” (weights/state) components are nullified.

Intuitively: **every meaningful nullification is an act of breaking mirror symmetry**, and chirality is the native carrier of the subject–instrument duality in GRA.

---

## 2. Формальная математика (кратко) / Formal math (short)

### 2.1. Хиральность / Chirality

**RU**

Пусть \(X\) — множество объектов, \(Z : X \to X\) — оператор «зеркала», а \(\mathcal{R}\) — семейство допустимых автоморфизмов (например, вращения).

Объект \(x \in X\) **хирален**, если

\[
\forall \rho \in \mathcal{R} \quad \rho(x) \neq Z(x).
\]

Тогда:

- правая конфигурация: \(\mathcal{R}(x) = x\),
- левая конфигурация: \(\mathcal{L}(x) = Z(x)\),
- пара \((\mathcal{R}(x), \mathcal{L}(x))\) — **хиральная пара**.

---

**EN**

Let \(X\) be a set of objects, \(Z : X \to X\) a “mirror” operator, and \(\mathcal{R}\) a family of admissible automorphisms (e.g. rotations).

An object \(x \in X\) is **chiral** if

\[
\forall \rho \in \mathcal{R} \quad \rho(x) \neq Z(x).
\]

Then:

- right configuration: \(\mathcal{R}(x) = x\),
- left configuration: \(\mathcal{L}(x) = Z(x)\),
- the pair \((\mathcal{R}(x), \mathcal{L}(x))\) is a **chiral pair**.

---

### 2.2. GRA‑обнулёнка как оператор / GRA nullification as an operator

**RU**

Рассмотрим тройку

\[
(\Pi, W, S),
\]

где:

- \(\Pi\) — политика/оператор (policy),
- \(W\) — вектор весов,
- \(S\) — состояние.

**Оператор обнулёнки** \(\mathcal{N}\) определяется как

\[
\mathcal{N} : \mathcal{P} \times \mathcal{W} \times \mathcal{S}
\rightarrow
\mathcal{P} \times \mathcal{W} \times \mathcal{S},
\]

\[
\mathcal{N}(\Pi, W, S) = (\Pi', 0, 0),
\]

где \(\Pi' = F(\Pi)\) — переparameterизованная политика.

---

**EN**

Take a triple

\[
(\Pi, W, S),
\]

where:

- \(\Pi\) is a policy/operator,
- \(W\) is a weight vector,
- \(S\) is a state.

The **nullification operator** \(\mathcal{N}\) is defined as

\[
\mathcal{N} : \mathcal{P} \times \mathcal{W} \times \mathcal{S}
\rightarrow
\mathcal{P} \times \mathcal{W} \times \mathcal{S},
\]

\[
\mathcal{N}(\Pi, W, S) = (\Pi', 0, 0),
\]

where \(\Pi' = F(\Pi)\) is a reparameterized policy.

---

### 2.3. Эквивалентность: хиральность = обнулёнка / Equivalence: chirality = nullification

**RU**

Если трактовать \(\Pi\) как правую конфигурацию, а \(Z(\Pi)\) — как левую, то можно положить

\[
F(\Pi) = (\Pi, Z(\Pi)) = (R, L).
\]

Тогда

\[
\mathcal{N}(\Pi, W, S) = ((\Pi, Z(\Pi)), 0, 0) = ((R, L), 0, 0),
\]

то есть **обнулёнка** есть переход в **хиральное пространство** с последующим занулением «массы» (весов и состояния).

---

**EN**

If we interpret \(\Pi\) as the right configuration and \(Z(\Pi)\) as the left one, we can define

\[
F(\Pi) = (\Pi, Z(\Pi)) = (R, L).
\]

Then

\[
\mathcal{N}(\Pi, W, S) = ((\Pi, Z(\Pi)), 0, 0) = ((R, L), 0, 0),
\]

i.e. **nullification** becomes a lift into **chiral space** followed by nullifying the “mass” (weights and state).

---

## 3. Структура репозитория / Repository structure

```text
GRA-Chiral-Nullification-Math/
├── README.md
├── LICENSE
├── requirements.txt
├── setup.py
├── src/
│   └── gra_chiral_null/
│       ├── __init__.py
│       ├── chirality_formalism.py
│       ├── gra_null_operator.py
│       ├── chiral_gra_equivalence.py
│       └── metrics_and_examples.py
├── docs/
│   ├── 01-intro.md
│   ├── 02-chirality-math.md
│   ├── 03-gra-nullification-math.md
│   ├── 04-chiral-gra-bridge.md
│   ├── 05-examples-and-use-cases.md
│   └── 06-future-work.md
├── notebooks/
│   ├── 01-chiral-sets-and-operators.ipynb
│   ├── 02-gra-null-as-operator.ipynb
│   └── 03-chiral-gra-equivalence.ipynb
├── tests/
│   ├── test_chirality_formalism.py
│   ├── test_gra_null_operator.py
│   └── test_chiral_gra_equivalence.py
└── frontend/
    └── app.py
```

**RU (кратко):**

- `src/gra_chiral_null/` — строгая математика: хиральность, обнуляющий оператор, эквивалентность.
- `docs/` — теоретические заметки и формальные выкладки.
- `notebooks/` — интерактивные демонстрации в виде Jupyter notebook.
- `tests/` — юнит‑тесты для базовой верификации аксиоматики.
- `frontend/` — простой веб-интерфейс (Streamlit) для интерактивной игры с хиральными парами и обнулёнкой.

**EN (short):**

- `src/gra_chiral_null/` — strict math: chirality, nullification operator, equivalence.
- `docs/` — theoretical notes and formal derivations.
- `notebooks/` — interactive Jupyter demonstrations.
- `tests/` — unit tests for basic axiomatic checks.
- `frontend/` — simple Streamlit web UI for playing with chiral pairs and nullification.

---

## 4. Быстрый старт / Quick start

**RU**

```bash
git clone https://github.com/qqewq/GRA-Chiral-Nullification-Math
cd GRA-Chiral-Nullification-Math

pip install -r requirements.txt
python -m pytest tests/
streamlit run frontend/app.py
```

**EN**

```bash
git clone https://github.com/qqewq/GRA-Chiral-Nullification-Math
cd GRA-Chiral-Nullification-Math

pip install -r requirements.txt
python -m pytest tests/
streamlit run frontend/app.py
```

---

## 5. Связь с GRA-экосистемой / Relation to the GRA ecosystem

**RU**

Этот репозиторий играет роль **математического ядра** для:

- [GRA-Meta-Nulling-Foundations](https://github.com/qqewq/GRA-Meta-Nulling-Foundations)
- [GRA-SubjectSwap](https://github.com/qqewq/GRA-SubjectSwap)
- [GRA-ASI-Metric-Space](https://github.com/qqewq/GRA-ASI-Metric-Space)
- [GRA-Quantum-Poetry](https://github.com/qqewq/gra-quantum-poetry)
- а также других GRA‑репозиториев, где требуется строгий язык обнулёнки.

Все они могут импортировать `gra_chiral_null` как **каноническую библиотеку хиральной обнулёнки**.

---

**EN**

This repository serves as a **mathematical core** for:

- [GRA-Meta-Nulling-Foundations](https://github.com/qqewq/GRA-Meta-Nulling-Foundations)
- [GRA-SubjectSwap](https://github.com/qqewq/GRA-SubjectSwap)
- [GRA-ASI-Metric-Space](https://github.com/qqewq/GRA-ASI-Metric-Space)
- [GRA-Quantum-Poetry](https://github.com/qqewq/gra-quantum-poetry)
- and other GRA repositories that require a strict nullification language.

All of them can import `gra_chiral_null` as the **canonical chiral nullification library**.

---

## 6. Лицензия / License

- **RU:** Проект распространяется по лицензии MIT. См. файл `LICENSE`.  
- **EN:** This project is released under the MIT License. See the `LICENSE` file.