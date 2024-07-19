from diffusers import AutoPipelineForText2Image, StableDiffusionXLPipeline, EulerAncestralDiscreteScheduler
from diffusers.models.autoencoders.vq_model import VQEncoderOutput, VQModel
import torch
import gc

# APIではなく本機で動かすため動作が重いCPU, memoryがかなり必要
def sdxl_turbo(prompt):
    # device = "cuda" if torch.cuda.is_available() else "cpu"
    device = "cpu"
    pipe = AutoPipelineForText2Image.from_pretrained(
        "stabilityai/sdxl-turbo", 
        torch_dtype=torch.float32, 
        # variant="fp16", 
        low_cpu_mem_usage=True
    )
    pipe.to(device)
    image = pipe(prompt=prompt, num_inference_steps=2, guidance_scale=0).images[0]
    
    # メモリを開放する
    del pipe
    gc.collect()    
    return image

def sdxl_anime(prompt):
    pipe = StableDiffusionXLPipeline.from_single_file("https://huggingface.co/martyn/sdxl-turbo-mario-merge-top-rated/blob/main/topRatedTurboxlLCM_v10.safetensors")
    pipe.to("cpu")
    pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)
    # Load the LoRA
    pipe.load_lora_weights('ntc-ai/SDXL-LoRA-slider.anime', weight_name='anime.safetensors', adapter_name="anime")
    # Activate the LoRA
    pipe.set_adapters(["anime"], adapter_weights=[2.0])
    negative_prompt = "nsfw"
    width = 512
    height = 512
    num_inference_steps = 4
    guidance_scale = 2
    image = pipe(prompt, negative_prompt=negative_prompt, width=width, height=height, guidance_scale=guidance_scale, num_inference_steps=num_inference_steps).images[0]
    del pipe
    torch.cuda.empty_cache()
    return image