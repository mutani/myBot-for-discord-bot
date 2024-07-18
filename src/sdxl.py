from diffusers import AutoPipelineForText2Image
import torch

def sdxl_turbo(prompt):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    device = "cpu"
    pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float32, variant="fp16")
    pipe.to(device)
    image = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]
    return image