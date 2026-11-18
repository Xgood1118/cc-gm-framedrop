# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import framedrop as mod  # noqa: E402


def test_plan_length():
    frames = framedrop.load_stats("data/stats.json")
    plan = framedrop.plan_schedule(frames, 60)
    assert len(plan) >= len([f for f in frames if not f.dropped])


def test_clock_error_bounded():
    frames = framedrop.load_stats("data/stats.json")
    plan = framedrop.plan_schedule(frames, 60)
    err = framedrop.clock_error(plan, frames)
    assert abs(err) < 500
