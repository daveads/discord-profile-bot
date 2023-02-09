import discord
from core.config_parser import BotConfigs


bot_configs = BotConfigs()


async def get_element(array):
    element = None
    for i in range(len(array)):
        if array[i] == True:
            element = i
            #print(i)
               
    return element



async def gender(interaction):    
    #gender roles id
    role_male =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("male")) 
    role_female =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("female"))
    role_trans_female =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("trans_female"))
    role_non_binary =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("non_binary"))
    role_agender =  discord.utils.get(interaction.guild.roles, id=bot_configs.gender("agender"))
    role_bigender = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("bigender"))
    role_genderfluid = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("genderfluid"))
    role_t_ftm = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("t_ftm"))
    role_t_mtf = discord.utils.get(interaction.guild.roles, id=bot_configs.gender("t_mtf"))

    genObj = [role_male, role_female, role_trans_female, role_non_binary, role_agender, role_bigender, role_genderfluid, role_t_ftm, role_t_mtf]
    
    return genObj




async def age(interaction):
    #age roles 
    a18_21 = discord.utils.get(interaction.guild.roles, id=bot_configs.age('18-21')) 
    a22_25 = discord.utils.get(interaction.guild.roles, id=bot_configs.age('22-25')) 
    a26_30 = discord.utils.get(interaction.guild.roles, id=bot_configs.age('26-30')) 
    a31    = discord.utils.get(interaction.guild.roles, id=bot_configs.age('31+'))

    ageObj = [a18_21, a22_25, a26_30, a31]
    return ageObj




async def orientation(interaction):
    hetorsexual = discord.utils.get(interaction.guild.roles, id=bot_configs.orientaion('hetorsexual'))
    homosexual = discord.utils.get(interaction.guild.roles, id=bot_configs.orientaion('homosexual'))
    bisexual = discord.utils.get(interaction.guild.roles, id=bot_configs.orientaion('bisexual'))
    pansexual = discord.utils.get(interaction.guild.roles, id=bot_configs.orientaion('pansexual'))
    asexual = discord.utils.get(interaction.guild.roles, id=bot_configs.orientaion('asexual'))
    demisexual = discord.utils.get(interaction.guild.roles, id=bot_configs.orientaion('demisexual'))
    bicurious = discord.utils.get(interaction.guild.roles, id=bot_configs.orientaion('bicurious'))
    
    oriObj = [hetorsexual, homosexual, asexual, bicurious, bisexual, demisexual, pansexual]

    return oriObj

#datingstatus  dmstatus height_roles



async def dmstatus(interaction):
    
    dmOpen = discord.utils.get(interaction.guild.roles, id=bot_configs.dmstatus('dmOpen'))
    dmOpenNoNsfw =discord.utils.get(interaction.guild.roles, id=bot_configs.dmstatus('dmOpenNoNsfw'))
    dmAsk = discord.utils.get(interaction.guild.roles, id=bot_configs.dmstatus('dmAsk'))
    dmOpenVerifiedOnly = discord.utils.get(interaction.guild.roles, id=bot_configs.dmstatus('dmOpenVerifiedOnly'))
    dmClosed = discord.utils.get(interaction.guild.roles, id=bot_configs.dmstatus('dmClosed'))
    
    dsObj = [dmAsk, dmClosed, dmOpen, dmOpenNoNsfw, dmOpenVerifiedOnly]

    return dsObj 



async def datingstatus(interaction):

    single = discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("single"))
    taken =discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("taken"))
    complicated = discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("complicated"))
    searching = discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("searching"))
    nsearching = discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("nsearching"))
    polyamorous = discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("polyamorous"))
    married = discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("married"))
    in_a_relatiohship = discord.utils.get(interaction.guild.roles, id=bot_configs.datingstatus("in_a_relatiohship"))


    dsObj = [single, taken, complicated, searching, nsearching, polyamorous, married, in_a_relatiohship]

    return dsObj



async def height(interaction):

    H4_6_4_8 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H4_6_4_8'))
    H4_8_4_10 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H4_8_4_10'))
    H4_10_5_0 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H4_10_5_0'))
    H5_0_5_2 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_0_5_2'))
    H5_2_5_4 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_2_5_4'))
    H5_4_5_6 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_4_5_6'))
    H5_6_5_8 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_6_5_8'))
    H5_8_5_10 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_8_5_10'))
    H5_10_6_0 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H5_10_6_0'))
    H6_0_6_2 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H6_0_6_2'))
    H6_2_6_4 = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H6_2_6_4'))
    H6_4_ = discord.utils.get(interaction.guild.roles, id=bot_configs.height('H6_4_'))

    heigObj = [H4_6_4_8, H4_8_4_10, H4_10_5_0, H5_0_5_2, H5_2_5_4, H5_4_5_6, H5_6_5_8, H5_8_5_10, H5_10_6_0, H6_0_6_2, H6_2_6_4, H6_4_] 

    """
    4'6-4'8 |     137-142cm
        4'8- 4'10 |   142-147cm
        4'10 - 5'10 | 147-152cm
        5'0 - 5'2 |   152-157cm
        5'2 - 5'4 |   157-162cm
        5'4 - 5'8 |   162-167cm
        5'8 - 5'10 |  167-177cm
        5'10 - 6'0 |  177-182cm
        6'0 - 6'2 |   182-187cm
        6'2 - 6'4 |   187-193cm
        6'4+ | 193cm+
        """

    return heigObj
