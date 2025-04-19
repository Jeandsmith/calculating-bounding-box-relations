# Interior Points, Epsilon, and Bounding Boxes

- We can determine the **internal** points in ranges of a set.
- We can set epsilon to any non-negative value `ε > 0`

## Initial Points of a Set

**Initial points** refer to the starting values of intervals within a set.

### Example:
Let **A = [1, 3) ∪ (4, 6] ∪ {8}**

- Interval [1, 3): starts at **1**
- Interval (4, 6]: starts just after **4**
- Singleton {8}: has 8 as both an initial and terminal point

**Initial points of A**: `{1, 4, 8}`

---

## Interior (Internal) Points

A point **x** is an interior point of a set **A** if:

> There exists some **ε > 0** such that **(x - ε, x + ε) ⊆ A**

This means a small open interval around **x** lies entirely within the set.

### Examples:
- **x = 2** in **A = [1, 3)** → interior point (e.g., ε = 0.5 gives (1.5, 2.5) ⊆ A)
- **x = 1** → not interior (any ε includes points < 1, which aren't in A)

---

## Choosing Epsilon (ε)

- You only need to find **one** ε > 0 that works.
- ε is **not fixed**—it can be different for each point.
- If **no ε** exists that satisfies the condition, the point is **not** interior.

---

## What Does ⊆ Mean?

- **⊆** = "is a subset of" or "is contained in"
- For example:
  - (x - ε, x + ε) ⊆ A → the entire interval is within the set A

---

## Interior Points in 2D and Bounding Boxes (bboxes)

### Bounding Box Basics:

A **bounding box (bbox)** is defined as:

```
bbox = [x_min, y_min, x_max, y_max]
```

It represents a rectangle in 2D space.

---

### Checking Interior Points in a Bbox:

A point **(x, y)** is an **interior point** of a bbox if:

> There exists ε > 0 such that  
> **(x - ε, x + ε) × (y - ε, y + ε) ⊆ bbox**

- **×** here is a Cartesian product, meaning a small square centered at (x, y)

---

### Visual Explanation (Text-Based):

```
Y ↑
  |                          (10,10)
  |-----------------------------+
  |                             |
  |            +---------------+ ← small square
  |            |     (5,5)     |
  |            +---------------+
  |                             |
  +-----------------------------+→ X
(0,0)
```

If (5,5) is the point and bbox = [0, 0, 10, 10],  
Then a small square like (4, 6) × (4, 6) fits inside → (5,5) is interior

---

## Checking If One Bbox is Inside Another

### Let:
- Bbox A = [x1_A, y1_A, x2_A, y2_A]
- Bbox B = [x1_B, y1_B, x2_B, y2_B]

### A is inside B if:
```
x1_B ≤ x1_A and x2_A ≤ x2_B
y1_B ≤ y1_A and y2_A ≤ y2_B
```

### A is **strictly** inside B (no edges touching) if:
```
x1_B < x1_A and x2_A < x2_B
y1_B < y1_A and y2_A < y2_B
```

---

## Using Distance to Determine Epsilon

For point (x, y) inside bbox [x1, y1, x2, y2]:

```text
ε_x = min(x - x1, x2 - x)
ε_y = min(y - y1, y2 - y)
ε = min(ε_x, ε_y)
```

This ensures a square centered at (x, y) stays fully inside the bbox.

---

## Bonus: What Does ∃ Mean?

- **∃** means **"there exists"**
- Common in definitions like:

  > ∃ ε > 0 such that (x - ε, x + ε) ⊆ A

- Often paired with:
  - **∀** → "for all"

---

## Summary

- Interior points are those with “room to wiggle” inside the set.
- ε is flexible, unique per point, and doesn’t need to be small or the same across points.
- The Cartesian product describes small square areas around a point.
- Bounding box containment uses simple coordinate comparisons.
- The minimum distance to an edge can guide ε selection in 2D.