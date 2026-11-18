# -*- coding: utf-8 -*-
"""丢帧补偿与播放时钟"""

from dataclasses import dataclass


@dataclass
class FrameStat:
    """一帧的到达与时间戳。"""
    index: int
    pts_ms: int
    arrive_ms: int
    dropped: bool = False




def load_stats(path):
    """读帧统计"""
    raise NotImplementedError("load_stats 尚未实现")


def plan_schedule(frames, target_fps):
    """生成显示计划"""
    raise NotImplementedError("plan_schedule 尚未实现")


def clock_error(plan, frames):
    """算时钟误差"""
    raise NotImplementedError("clock_error 尚未实现")

