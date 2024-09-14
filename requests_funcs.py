from aiogram import Router
import requests


router = Router()


url = 'https://modelslab.com/api/v6/images/text2img'


async def get_img_from_txt(prompt: str):
    data = {
      "key": "OvypnElGk8xfI9Zo7k2SBHXowjXPG93FlgsHn9tkSDR8e2wqAkHbVFpNdy49",
      "model_id": "sdxlceshi",
      "prompt": f"car, {prompt}, photography, real, realistic, 8k, photorealistic, ultra detailed, ultra textured, volumetric lighting",
      "negative_prompt": "",
      "width": "1024",
      "height": "1024",
      "samples": "1",
      "num_inference_steps": "31",
      "safety_checker": "no",
      "enhance_prompt": "yes",
      "seed": None,
      "guidance_scale": 7.5,
      "panorama": "no",
      "self_attention": "no",
      "upscale": "no",
      "embeddings_model": None,
      "lora_model": None,
      "tomesd": "yes",
      "clip_skip": "2",
      "use_karras_sigmas": "yes",
      "vae": None,
      "lora_strength": None,
      "scheduler": "UniPCMultistepScheduler",
      "webhook": None,
      "track_id": None
    }
    response = requests.post(url, data=data)
    if response.status_code == 200:
        response_data = response.json()
        print(response_data)
        if response_data['output'] and response_data['output'][0]:
            return response_data['output'][0]
        elif response_data['future_links'] and response_data['future_links'][0]:
            return response_data['future_links'][0]
        else:
            return 'Ошибка выполнения запроса!'
    else:
        return 'Ошибка выполнения запроса!'