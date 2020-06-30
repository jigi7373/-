import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswith("시발"):
        await message.channel.send("↑사람이 시발이라는 욕을 사용했습니다")
    if message.content.startswith("씨발"):
        await message.channel.send("↑사람이 시발이라는 욕을 사용했습니다")
    if message.content.startswith("tlqkf"):
        await message.channel.send("↑사람이 시발이라는 욕을 사용했습니다")
    if message.content.startswith("Tlqkf"):
        await message.channel.send("↑사람이 시발이라는 욕을 사용했습니다")
    if message.content.startswith("ㅅㅂ"):
        await message.channel.send("↑사람이 시발이라는 욕을 사용했습니다")
    if message.content.startswith("씨바"):
        await message.channel.send("↑사람이 시발이라는 욕을 사용했습니다")
    if message.content.startswith("닥쳐"):
        await message.channel.send("↑사람이 닥쳐라는 욕을 사용했습니다")
    if message.content.startswith("ekrcu"):
        await message.channel.send("↑사람이 닥쳐라는 욕을 사용했습니다")
    if message.content.startswith("아가리해"):
        await message.channel.send("↑사람이 닥쳐라는 욕을 사용했습니다")
    if message.content.startswith("아가리 싸물어"):
        await message.channel.send("↑사람이 닥쳐라는 욕을 사용했습니다")
    if message.content.startswith("미친"):
        await message.channel.send("↑사람이 미친이라는 욕을 사용했습니다")
    if message.content.startswith("밑힌"):
        await message.channel.send("↑사람이 미친이라는 욕을 사용했습니다")
    if message.content.startswith("alcls"):
        await message.channel.send("↑사람이 미친이라는 욕을 사용했습니다")
    if message.content.startswith("및니"):
        await message.channel.send("↑사람이 미친이라는 욕을 사용했습니다")
    if message.content.startswith("및닠"):
        await message.channel.send("↑사람이 미친이라는 욕을 사용했습니다")
    if message.content.startswith("ㅁㅊ"):
        await message.channel.send("↑사람이 미친이라는 욕을 사용했습니다")










client.run("NzI3MTU5ODk5MTQ1ODk1OTU4.Xvp_bw.cdDWBXtOjSd7RxAQ8F07HF-qisQ")