import pandas as pd
import math
import discord
from discord.ext import commands

token = open("bot-token", "r").readline()

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('We have logged in as {}'.format(bot))
    print('Bot name: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))
    
@bot.command(name='addrole', hidden=True)
@commands.has_permissions(administrator=True)
async def add_role(ctx):
    total_role_granted = 0
    total_gleam_joined = 0
    total_abuse_user = 0
    total_empty_discordId = 0
    total_not_joined = 0
    empty_discordId_user_list = 'Chekc CSV File Line : '
    
    gleam_result = pd.read_csv('./gleam-result.csv', engine='python', dtype={"DiscordId" : object})
    gleam_result.head()
    
    for idx,row in gleam_result.iterrows():
        gleam_user_name = row[0]
        secret_code = row[1]
        discord_id = row[2]
        total_gleam_joined+=1
        
        if (secret_code == 'OASYSBCG' or 'CARVANDOASYS'
            or 'OASYSBCG82' or 'OASYSBCGYGG' or 'OASYSBCGSF' or 'OASYSVIETNAM'
            or 'OASYSBCGRDD' or 'OASYSBCGGTP' or 'OASYSBCGNAKJU' or 'OASYSBCGGMD') :
                
                if (math.isnan(float(discord_id)) == False) : 
                    cast_discordId = int(discord_id)

                    member = discord.utils.find(lambda member : member.id == cast_discordId, ctx.guild.members)
                    role = discord.utils.find(lambda role : role.name == "AMA TRAVELER", ctx.guild.roles)
 
                    if role is not None :
                        if member is not None :
                            await member.add_roles(role)
                            total_role_granted+=1
                        
                        else :
                            total_not_joined+=1
                
                else : 
                    total_empty_discordId+=1
                    empty_discordId_user_list+=','+str(idx+1)
                          
        else :               
            total_abuse_user+=1

    embed=discord.Embed(title="Command Execution Results", description="Command : !addrole", color=0x348fd5)
    embed.add_field(name="Total gleam participants", value=total_gleam_joined, inline=False)
    embed.add_field(name="Total role-granted users", value=total_role_granted, inline=True)
    embed.add_field(name="Total number of abusers", value=total_abuse_user, inline=True)
    embed.add_field(name="Total who did not joined Oasys Discord", value=total_not_joined, inline=True)
    embed.add_field(name="Total who did not submit a discord Id", value=total_empty_discordId, inline=False)
    embed.add_field(name="List of users who did not submit a discord Id", value=empty_discordId_user_list, inline=False)
    await ctx.send(embed=embed)
                    
bot.run(token)

