"""
Flow 1 Tasks - Step 1, Step 2, Step 3
"""

import time
from typing import Any, Dict

from prefect import get_run_logger, task


@task(name="step-1", retries=2)
def step_1(message: str) -> Dict[str, Any]:
    """Step 1: Initial processing"""
    logger = get_run_logger()

    logger.info("🚀 FLOW 1 - Starting Step 1")
    logger.info(f"📝 Input message: {message}")

    # Simulate some work
    time.sleep(2)

    result = {
        "step": "step_1",
        "status": "completed",
        "message": f"Step 1 processed: {message}",
        "data": {"count": 10, "type": "initial"},
    }

    logger.info("✅ FLOW 1 - Step 1 completed successfully")
    logger.info(f"📊 Step 1 result: {result}")

    return result


@task(name="step-2", retries=2)
def step_2(step1_result: Dict[str, Any]) -> Dict[str, Any]:
    """Step 2: Processing step 1 results"""
    logger = get_run_logger()

    logger.info("🔄 FLOW 1 - Starting Step 2")
    logger.info(f"📥 Received from Step 1: {step1_result}")

    # Simulate some work
    time.sleep(3)

    # Process the data from step 1
    previous_count = step1_result.get("data", {}).get("count", 0)
    new_count = previous_count * 2

    result = {
        "step": "step_2",
        "status": "completed",
        "message": "Step 2 processed data from Step 1",
        "data": {
            "previous_count": previous_count,
            "new_count": new_count,
            "type": "processed",
        },
        "step1_reference": step1_result["message"],
    }

    logger.info("✅ FLOW 1 - Step 2 completed successfully")
    logger.info(f"📊 Step 2 result: {result}")

    return result


@task(name="step-3", retries=2)
def step_3(
    step1_result: Dict[str, Any], step2_result: Dict[str, Any]
) -> Dict[str, Any]:
    """Step 3: Final processing with results from both previous steps"""
    logger = get_run_logger()

    logger.info("🏁 FLOW 1 - Starting Step 3 (Final Step)")
    logger.info(f"📥 Received from Step 1: {step1_result}")
    logger.info(f"📥 Received from Step 2: {step2_result}")

    # Simulate some work
    time.sleep(1)

    # Combine results from both steps
    step1_count = step1_result.get("data", {}).get("count", 0)
    step2_count = step2_result.get("data", {}).get("new_count", 0)
    final_count = step1_count + step2_count

    result = {
        "step": "step_3",
        "status": "completed",
        "message": "Flow 1 pipeline completed successfully",
        "data": {
            "step1_count": step1_count,
            "step2_count": step2_count,
            "final_count": final_count,
            "type": "final",
        },
        "summary": {
            "total_steps": 3,
            "flow_name": "Flow 1 - Simple Pipeline",
            "all_steps_completed": True,
        },
    }

    logger.info("🎉 FLOW 1 - Step 3 completed successfully")
    logger.info("✅ FLOW 1 - All steps completed!")
    logger.info(f"📊 Final result: {result}")

    return result
