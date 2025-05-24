"""
Flow 2 Tasks - Step A, Step B, Step C
"""

from prefect import task, get_run_logger
import time
from typing import Dict, Any


@task(name="step-a", retries=2)
def step_a(message: str) -> Dict[str, Any]:
    """Step A: Data collection"""
    logger = get_run_logger()

    logger.info("🔍 FLOW 2 - Starting Step A")
    logger.info(f"📝 Input message: {message}")

    # Simulate data collection
    time.sleep(2)

    collected_data = [
        {"id": 1, "value": "apple", "category": "fruit"},
        {"id": 2, "value": "carrot", "category": "vegetable"},
        {"id": 3, "value": "banana", "category": "fruit"},
    ]

    result = {
        "step": "step_a",
        "status": "completed",
        "message": f"Step A collected data: {message}",
        "data": {
            "collected_items": collected_data,
            "total_items": len(collected_data),
            "collection_type": "sample_data",
        },
    }

    logger.info("✅ FLOW 2 - Step A completed successfully")
    logger.info(f"📊 Step A collected {len(collected_data)} items")

    return result


@task(name="step-b", retries=2)
def step_b(step_a_result: Dict[str, Any]) -> Dict[str, Any]:
    """Step B: Data transformation"""
    logger = get_run_logger()

    logger.info("🔧 FLOW 2 - Starting Step B")
    logger.info(f"📥 Received from Step A: {step_a_result}")

    # Simulate data transformation
    time.sleep(3)

    # Transform the data from step A
    collected_items = step_a_result.get("data", {}).get("collected_items", [])

    # Group by category
    fruits = [item for item in collected_items if item["category"] == "fruit"]
    vegetables = [item for item in collected_items if item["category"] == "vegetable"]

    transformed_data = {
        "fruits": fruits,
        "vegetables": vegetables,
        "fruit_count": len(fruits),
        "vegetable_count": len(vegetables),
    }

    result = {
        "step": "step_b",
        "status": "completed",
        "message": "Step B transformed data from Step A",
        "data": {
            "transformed_data": transformed_data,
            "transformation_type": "category_grouping",
            "original_count": len(collected_items),
        },
        "step_a_reference": step_a_result["message"],
    }

    logger.info("✅ FLOW 2 - Step B completed successfully")
    logger.info(
        f"📊 Step B transformed data: {transformed_data['fruit_count']} fruits, {transformed_data['vegetable_count']} vegetables"
    )

    return result


@task(name="step-c", retries=2)
def step_c(
    step_a_result: Dict[str, Any], step_b_result: Dict[str, Any]
) -> Dict[str, Any]:
    """Step C: Final analysis and reporting"""
    logger = get_run_logger()

    logger.info("📊 FLOW 2 - Starting Step C (Final Analysis)")
    logger.info(f"📥 Received from Step A: {step_a_result}")
    logger.info(f"📥 Received from Step B: {step_b_result}")

    # Simulate analysis
    time.sleep(1)

    # Analyze results from both steps
    original_items = step_a_result.get("data", {}).get("total_items", 0)
    transformed_data = step_b_result.get("data", {}).get("transformed_data", {})

    analysis = {
        "total_processed": original_items,
        "fruits_found": transformed_data.get("fruit_count", 0),
        "vegetables_found": transformed_data.get("vegetable_count", 0),
        "processing_efficiency": "100%",
        "data_quality": "high",
    }

    result = {
        "step": "step_c",
        "status": "completed",
        "message": "Flow 2 analysis pipeline completed successfully",
        "data": {"analysis": analysis, "analysis_type": "final_report"},
        "summary": {
            "total_steps": 3,
            "flow_name": "Flow 2 - Another Pipeline",
            "all_steps_completed": True,
            "step_sequence": [
                "Step A: Collection",
                "Step B: Transformation",
                "Step C: Analysis",
            ],
        },
    }

    logger.info("🎉 FLOW 2 - Step C completed successfully")
    logger.info("✅ FLOW 2 - All steps completed!")
    logger.info(f"📊 Final analysis: {analysis}")

    return result
