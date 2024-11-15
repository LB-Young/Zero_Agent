import asyncio
from domain_expert_team.leader import Leader
from llm_client import client, model

async def main():
    with open(r"F:\Cmodels\Zero_Agent\roleplay_onestep\job_describe.txt", "r", encoding="utf-8") as f:
        job_describe = f.read()
    leader = Leader(role_leader=job_describe, agents=None, client=client, model=model)
    with open(r"C:\Users\86187\Desktop\test.txt", "r", encoding="utf-8") as f:
        reference = f.read()
    query = f"请根据以下参考信息回答问题：\n{reference}\n\n问题：介绍一下这篇文章的内容"
    # result = await leader.execute("我是高考生，现在想要选专业，但是不知道选什么专业。请你介绍一下金融、法律和计算机三个专业分别有什么优点和缺点。")
    all_response = ""
    async for item in leader.execute(qeury=query):
        all_response += item
        print(item, end="", flush=True)


    audio = input("是否生成音频？y/n:")
    if audio.strip() == "y":
        from text_to_audio import text_to_audio
        from audio_play import play_audio
        all_roles_map = {"host":"xiaoyan",
                        "expert":"aisjiuxu",
                        "self":"aisjinger"}
        all_response_lists = all_response.split("=>@")
        for item in all_response_lists:
            if item.strip().startswith("host"):
                text_to_audio(item.split(":",1)[-1].strip(), all_roles_map["host"])
            elif item.strip().startswith("expert"):
                text_to_audio(item.split(":",1)[-1].strip(), all_roles_map["expert"])
            elif item.strip().startswith("self"):
                text_to_audio(item.split(":",1)[-1].strip(), all_roles_map["self"])
            else:
                print(item, "aisbabyxu")
            import time
            time.sleep(100)
    audio_play = input("是否播放音频？y/n:")
    if audio_play.strip() == "y":
        role_audio_play_index = {
            "self":0,
            "expert":0,
            "host":0,
            "other":0
        }
        for item in all_response_lists:
            if item.strip().startswith("host"):
                play_audio(fr'F:\Cmodels\Zero_Agent\roleplay_onestep\audios\{all_roles_map["host"]}\{role_audio_play_index["host"]}.pcm')
                role_audio_play_index["host"] = role_audio_play_index["host"] + 1
            elif item.strip().startswith("expert"):
                play_audio(fr'F:\Cmodels\Zero_Agent\roleplay_onestep\audios\{all_roles_map["expert"]}\{role_audio_play_index["expert"]}.pcm')
                role_audio_play_index["expert"] = role_audio_play_index["expert"] + 1
            elif item.strip().startswith("self"):
                play_audio(fr'F:\Cmodels\Zero_Agent\roleplay_onestep\audios\{all_roles_map["self"]}\{role_audio_play_index["self"]}.pcm')
                role_audio_play_index["self"] = role_audio_play_index["self"] + 1
            else:
                pass
        
    # print(result)

if __name__ == "__main__":
    # TODO: Add a command line interface
    asyncio.run(main())