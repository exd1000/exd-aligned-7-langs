# 🐍 Python Method Categories (With Examples!)

Organized by **data type**, with clear subcategories and cute examples so you always know what you're working with 💻✨

***bc i'm the laziest person alive lmao***

---

## 🧠 `str` – String Methods

### 🔍 Check Methods
- `isalpha()` → `'hello'.isalpha()` ➝ `True`
- `isdigit()` → `'123'.isdigit()` ➝ `True`
- `isnumeric()` → `'⅕'.isnumeric()` ➝ `True`
- `islower()`, `isupper()`, `isspace()`, `istitle()`

### 🔄 Modify / Format
- `upper()`, `lower()`, `capitalize()`, `title()`
- `replace(old, new)` → `'sad'.replace('s', 'gl')` ➝ `'glad'`
- `strip()`, `lstrip()`, `rstrip()` → removes whitespace

### ✂️ Split / Join
- `split()` → `'a b c'.split()` ➝ `['a','b','c']`
- `' '.join(list)` → `' '.join(['hi', 'babe'])` ➝ `'hi babe'`

### 🎯 Search / Locate
- `find()`, `rfind()` → return index or `-1`
- `index()` → like `find()`, but errors if not found
- `startswith()`, `endswith()`

### 📐 Align / Pad
- `center(width)`, `ljust()`, `rjust()`
- `zfill(width)` → `'5'.zfill(3)` ➝ `'005'`

---

## 📦 `list` – List Methods

### ➕ Add / Remove
- `append(x)`, `extend(iterable)`, `insert(i, x)`
- `remove(x)` → removes first match
- `pop()` → removes and returns last item

### 🌀 Modify
- `reverse()`
- `sort()` → modifies in-place
- `copy()` → shallow copy

### 🔍 Inspect
- `count(x)`
- `index(x)`

---

## 🪵 `tuple` – Tuple Methods (Immutable)
- `count(x)`
- `index(x)`

---

## 🍃 `set` – Set Methods

### ➕ Add / Remove
- `add(x)`, `remove(x)`, `discard(x)`, `pop()`

### ⚔️ Set Logic
- `union(set)`, `intersection(set)`, `difference(set)`
- `symmetric_difference(set)`
- `issubset(set)`, `issuperset(set)`
- `update(set)`

---

## 📓 `dict` – Dictionary Methods

### 🧩 Add / Update / Access
- `get(key, default)`
- `setdefault(key, default)`
- `update({k: v})`

### 🔑 Keys / Values / Items
- `keys()`, `values()`, `items()`

### 🧹 Remove
- `pop(key)`, `popitem()` → removes last inserted
- `clear()` → wipes entire dict

---

## 🧮 `float` – Float-Specific Methods

### 🔍 Check
- `is_integer()` → `12.0.is_integer()` ➝ `True`

### 📐 Convert
- `as_integer_ratio()` → `0.5.as_integer_ratio()` ➝ `(1, 2)`
- `hex()`, `fromhex()`

---

## 🎛 Built-in Functions (Work Across Types)

### 🔍 Introspection / Info
- `len(x)`, `type(x)`, `id(x)`

### 🔁 Conversions
- `int()`, `float()`, `str()`, `list()`, `set()`, `dict()`

### 🎲 Iteration Helpers
- `enumerate()`, `zip()`, `map()`, `filter()`
- `range()`, `reversed()`
- `sorted()`

### 🧮 Math-ish
- `sum()`, `min()`, `max()`
- `abs()`, `round()`

---

## 🧠 How to Explore More

```python
# See all methods for a type:
dir(str), dir(list), dir(float)

# Get help on any method:
help(str.replace)
```
