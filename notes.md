# AreTheySame

This is from CodeWar.

## Description

> Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears). "Same" means, here, that the elements in b are the elements in a squared, regardless of the order. I case of empty or None the result is false.

## Notes

 ✅ - Done.
 🍅 - Pomodoro cycle.
 🔴 - Red.
 🟢 - Green.
 ♻️ - Refactor.
 💿 - Commit.

---

### Guardinas

- Input is two array. 🔴💿🟢💿
- Output is a boolean.
- Empty or None input gives false.
  
### Process

- We should divide element of 'a' with element of 'b' witout remainder. It gives true result.
