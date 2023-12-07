import json

# 读取JSON文件
with open("IEEE_journal.json", "r") as file:
    data = json.load(file)

# 计算每份的条数
batch_size = len(data) // 100

# 拆分成等份并保存到不同的文件中
for i in range(100):
    start_index = i * batch_size
    end_index = (i + 1) * batch_size
    if i == 99:  # 最后一份
        end_index = None
    batch_data = data[start_index:end_index]
    with open(f"documents/batch_{i+1}.json", "w") as file:
        json.dump(batch_data, file)