# 丢帧补偿与播放时钟

一个在丢帧环境下维持播放时钟稳定的调度器

## 保留签名

- `FrameStat`
- `load_stats(path)`
- `plan_schedule(frames, target_fps)`
- `clock_error(plan, frames)`

## 自测

```
python -m pytest tests -q
python -m framedrop.cli data/stats.json --out plan.json
```
