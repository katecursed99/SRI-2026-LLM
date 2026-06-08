model_prices = {
    # Free Tier
    "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning": {"in": 0.0, "out": 0.0},
    "baidu/ernie-4.5-0.3b": {"in": 0.0, "out": 0.0},

    # ~$0.03–0.06
    "openai/gpt-oss-20b": {"in": 0.041145, "out": 0.189735},
    "nvidia/nemotron-nano-9b-v2": {"in": 0.05486, "out": 0.21944},
    "openai/gpt-oss-120b": {"in": 0.05486, "out": 0.5486},

    # ~$0.06–0.13
    "nvidia/nemotron-3-nano-30b-a3b": {"in": 0.065, "out": 0.26},
    "openai/gpt-5-nano-2025-08-07": {"in": 0.065, "out": 0.52},
    # Expanded baidu/ernie-4.5-*
    "baidu/ernie-4.5-300b-a47b": {"in": 0.0936, "out": 0.3718},
    "baidu/ernie-4.5-300b-a47b-paddle": {"in": 0.0936, "out": 0.3718},
    "baidu/ernie-4-5-turbo-128k": {"in": 0.0936, "out": 0.3718},
    "baidu/ernie-4.5-21b-a3b": {"in": 0.0936, "out": 0.3718},
    "baidu/ernie-4.5-21b-a3b-thinking": {"in": 0.0936, "out": 0.3718},
    "nvidia/nemotron-3-super-120b-a12b": {"in": 0.117, "out": 0.585},
    "alibaba/qwen3.5-flash": {"in": 0.13, "out": 0.52},
    "bytedance/dola-seed-2-0-mini": {"in": 0.13, "out": 0.52},

    # ~$0.18–0.40
    "deepseek/deepseek-v4-flash": {"in": 0.182, "out": 0.364},
    "alibaba/qwen3-next-80b-a3b-instruct": {"in": 0.195, "out": 1.56},
    "moonshot/kimi-k2-0905-preview": {"in": 0.195, "out": 3.25},
    "alibaba/qwen3-32b": {"in": 0.208, "out": 0.832},
    "moonshot/kimi-k2-6": {"in": 0.208, "out": 5.2},
    # Expanded baidu/ernie-x1-*
    "baidu/ernie-x1-turbo-32k": {"in": 0.2145, "out": 0.858},
    "zhipu/glm-4.5-air": {"in": 0.26, "out": 1.43},
    "stepfun/step-3.7-flash": {"in": 0.26, "out": 1.495},
    "x-ai/grok-4-1-fast-non-reasoning": {"in": 0.26, "out": 0.65},
    "x-ai/grok-code-fast-1": {"in": 0.26, "out": 1.95},
    "alibaba/qwen3-vl-32b-instruct": {"in": 0.26, "out": 2.08},
    "deepseek/deepseek-chat-v3.1": {"in": 0.294, "out": 0.441},
    "alibaba/qwen3.6-flash": {"in": 0.325, "out": 1.95},
    "openai/gpt-5-mini-2025-08-07": {"in": 0.325, "out": 2.6},
    "openai/gpt-5-1-codex-mini": {"in": 0.325, "out": 2.6},
    "bytedance/dola-seed-2-0-lite": {"in": 0.325, "out": 2.6},
    "google/gemini-3-1-flash-lite-preview": {"in": 0.33, "out": 1.95},
    "alibaba/qwen3.6-35b-a3b": {"in": 0.375, "out": 2.25},
    "minimax/m2": {"in": 0.39, "out": 1.56},
    "minimax/m2-1": {"in": 0.39, "out": 1.56}, ###
    "xiaomi/mimo-v2.5": {"in": 0.4, "out": 2.0},
    "nousresearch/hermes-4-405b": {"in": 0.41145, "out": 1.6458},

    # ~$0.5–1.0
    "alibaba/qwen3.7-plus": {"in": 0.52, "out": 2.08},
    # Expanded x-ai/grok-4-fast-*
    "x-ai/grok-4-fast-non-reasoning": {"in": 0.52, "out": 1.3},
    "x-ai/grok-4-fast-reasoning": {"in": 0.52, "out": 1.3},
    "alibaba/qwen3.5-omni-flash": {"in": 0.52, "out": 2.86},
    "google/gemma-4-31b-it": {"in": 0.5486, "out": 0.5486},
    "bytedance/dola-seed-2-0-pro": {"in": 0.65, "out": 3.9},
    "bytedance/dola-seed-2-0-code": {"in": 0.65, "out": 3.9},
    "google/gemini-3-flash-preview": {"in": 0.65, "out": 3.9},
    "alibaba/qwen3.6-plus": {"in": 0.65, "out": 0.39},
    "openai/gpt-3.5-turbo": {"in": 0.50, "out": 1.50},
    # Expanded baidu/ernie-4.5-vl-*
    "baidu/ernie-4.5-vl-28b-a3b": {"in": 0.6435, "out": 1.859},
    "baidu/ernie-4.5-vl-424b-a47b": {"in": 0.6435, "out": 1.859},
    "baidu/ernie-4-5-turbo-vl-32k": {"in": 0.6435, "out": 1.859},
    "zhipu/glm-4.6": {"in": 0.78, "out": 2.86},
    "zhipu/glm-4.7": {"in": 0.78, "out": 2.86},
    "moonshot/kimi-k2-5": {"in": 0.78, "out": 3.9}, ###
    "alibaba/qwen3.6-27b": {"in": 0.78, "out": 4.68},
    "xiaomi/mimo-v2.5-pro": {"in": 1.0, "out": 3.0},
    "zhipu/glm-4.5": {"in": 0.60, "out": 2.2},


    # ~$1–3
    # Expanded baidu/ernie-5-0-*
    "baidu/ernie-5-0-thinking-preview": {"in": 1.2298, "out": 2.0449},
    "baidu/ernie-5-0-thinking-latest": {"in": 1.2298, "out": 2.0449},
    "x-ai/grok-build-0-1": {"in": 1.3, "out": 2.6},
    "zhipu/glm-5": {"in": 1.3, "out": 4.16},
    "anthropic/claude-haiku-4.5": {"in": 1.3, "out": 6.5},
    "openai/gpt-5-2025-08-07": {"in": 1.625, "out": 13.0},
    "openai/gpt-5-1": {"in": 1.625, "out": 13.0},
    "alibaba/qwen3.5-plus-20260218": {"in": 1.56, "out": 9.36},
    "alibaba/qwen3-max-preview": {"in": 1.56, "out": 7.8},
    "zhipu/glm-5-1": {"in": 1.82, "out": 5.72},
    "alibaba/qwen3.5-omni-plus": {"in": 1.82, "out": 10.79},
    "alibaba/qwen3-coder-480b-a35b-instruct": {"in": 1.95, "out": 9.75},
    "openai/gpt-5-2": {"in": 2.27, "out": 18.2},
    "deepseek/deepseek-v4-pro": {"in": 2.262, "out": 4.524},
    # Expanded x-ai/grok-4-20-*
    "x-ai/grok-4-20-0309-non-reasoning": {"in": 2.6, "out": 7.8},
    "x-ai/grok-4-20-0309-reasoning": {"in": 2.6, "out": 7.8},
    "google/gemini-3-1-pro-preview": {"in": 2.6, "out": 15.6},
    "alibaba/qwen3.6-max-preview": {"in": 1.69, "out": 10.14},

    # ~$3–10
    "alibaba/qwen3.7-max": {"in": 3.25, "out": 9.75},
    "google/gemini-3-5-flash": {"in": 3.25, "out": 23.4},
    "anthropic/claude-sonnet-4.6": {"in": 3.9, "out": 19.5},
    "perplexity/sonar-pro": {"in": 3.9, "out": 19.5}, ###

    # ~$6+ (premium)
    "openai/gpt-5-5": {"in": 6.5, "out": 39},
    # Expanded anthropic/claude-opus-4*
    "anthropic/claude-opus-4": {"in": 6.5, "out": 32.5},
    "anthropic/claude-opus-4-5": {"in": 6.5, "out": 32.5},
    "anthropic/claude-opus-4-6": {"in": 6.5, "out": 32.5},
    "anthropic/claude-opus-4-7": {"in": 6.5, "out": 32.5},
    "anthropic/claude-opus-4-8": {"in": 6.5, "out": 32.5},
    "anthropic/claude-opus-4.1": {"in": 19.5, "out": 97.5},
    "openai/gpt-5-2-pro": {"in": 27.3, "out": 218.4},
    "openai/gpt-5-4-pro": {"in": 39.0, "out": 234.0},
    "openai/gpt-5-5-pro": {"in": 39.0, "out": 234.0},
}

model_prices_sorted = []
current_index = 0


for model in model_prices: # loop through the original list
    # average the cost
    model_prices[model]["avg"] = (model_prices[model]["in"] + model_prices[model]["out"])/2
# sort by average cost with a lil lambda function
model_prices_sorted = sorted(
    model_prices.items(),
    key=lambda item: item[1]["avg"]
)

#print(model_prices_sorted)
