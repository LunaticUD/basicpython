# 列表：list
names: list[str] = ["a", "b"]
scores: list[float] = [0.1, 0.2]
items: list[int | str] = [1, "x"]          # 联合类型
# 字典：dict
pipelines: dict[str, Pipeline] = {"SVM": pipe1, "RF": pipe2}
params: dict[str, int] = {"n_estimators": 200}
grid: dict[str, list[int]] = {"n_estimators": [100, 200]}
# 集合：set
seen: set[str] = {"a", "b"}
# 元组：tuple
pair: tuple[str, int] = ("D7", 7)
triple: tuple[str, int, float] = ("x", 1, 0.5)
# Optional 用法
best_model_name: str | None = None
# 函数：fun
def add(a: int, b: int) -> int:
    return a + b

