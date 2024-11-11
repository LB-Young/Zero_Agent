import pyaudio
import wave
import os

class PCMPlayer:
    def __init__(self, channels=1, sample_width=2, sample_rate=16000):
        """
        初始化PCM播放器
        :param channels: 声道数
        :param sample_width: 采样宽度（字节）
        :param sample_rate: 采样率
        """
        self.channels = channels
        self.sample_width = sample_width
        self.sample_rate = sample_rate
        self.p = pyaudio.PyAudio()
        
    def play_pcm_file(self, pcm_file_path):
        """
        播放PCM文件
        :param pcm_file_path: PCM文件路径
        """
        try:
            # 打开PCM文件
            with open(pcm_file_path, 'rb') as pcm_file:
                pcm_data = pcm_file.read()
            
            # 创建音频流
            stream = self.p.open(format=self.p.get_format_from_width(self.sample_width),
                               channels=self.channels,
                               rate=self.sample_rate,
                               output=True)
            
            # 播放音频
            stream.write(pcm_data)
            
            # 清理
            stream.stop_stream()
            stream.close()
            
            print(f"完成播放: {pcm_file_path}")
            
        except Exception as e:
            print(f"播放出错: {str(e)}")
            
    def convert_to_wav(self, pcm_file_path, wav_file_path):
        """
        将PCM文件转换为WAV文件
        :param pcm_file_path: PCM文件路径
        :param wav_file_path: 输出WAV文件路径
        """
        try:
            # 读取PCM数据
            with open(pcm_file_path, 'rb') as pcm_file:
                pcm_data = pcm_file.read()
            
            # 创建WAV文件
            with wave.open(wav_file_path, 'wb') as wav_file:
                wav_file.setnchannels(self.channels)
                wav_file.setsampwidth(self.sample_width)
                wav_file.setframerate(self.sample_rate)
                wav_file.writeframes(pcm_data)
                
            print(f"转换完成: {wav_file_path}")
            
        except Exception as e:
            print(f"转换出错: {str(e)}")
    
    def __del__(self):
        """
        清理PyAudio资源
        """
        self.p.terminate()

# 使用示例
if __name__ == "__main__":
    # 创建PCM播放器实例
    player = PCMPlayer(channels=1,          # 单声道
                      sample_width=2,        # 16位采样
                      sample_rate=16000)     # 16kHz采样率
    
    # 播放PCM文件
    pcm_file = "F:\Cmodels\Zero_Agent\demo.pcm"
    if os.path.exists(pcm_file):
        player.play_pcm_file(pcm_file)
    
    # 转换为WAV文件（可选）
    # wav_file = "audio.wav"
    # player.convert_to_wav(pcm_file, wav_file)