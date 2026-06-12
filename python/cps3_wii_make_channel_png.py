# -- coding: UTF-8 --

from init_global_configs import Init_Global_Configs
from wii_channel_icon import rom_file_title_list
from wii_channel_icon import WiiChannel_Icon
from wii_channel_standard_banner import StandardBannerConfigs
from wii_channel_standard_banner import standard_banner_configs_list
from wii_channel_standard_banner import StandardBanner
from wii_channel_wide_banner import WideBannerConfigs
from wii_channel_wide_banner import wide_banner_configs_list
from wii_channel_wide_banner import WideBanner

if __name__ == "__main__":
    Init_Global_Configs()

    rom_file_title = "jojo"
    rom_file_title_list.append(rom_file_title)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        game_logo_size=(160, 80),
        game_logo_left_top=(418, 250),
        company_logo_left_top=StandardBannerConfigs.COMPANY_LOGO_ALIGN_RIGHT_TOP,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    wide_banner_configs = WideBannerConfigs(rom_file_title)
    wide_banner_configs_list.append(wide_banner_configs)

    rom_file_title = "jojoba"
    rom_file_title_list.append(rom_file_title)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        game_logo_size=(300, 150),
        # 靠右居中
        game_logo_left_top=(296, 122),
        company_logo_left_top=StandardBannerConfigs.COMPANY_LOGO_ALIGN_RIGHT_TOP,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    wide_banner_configs = WideBannerConfigs(
        rom_file_title,
        game_logo_size=(270, 150),
        # 靠下居中
        game_logo_left_top=(273, 182),
        company_logo_left_top=WideBannerConfigs.COMPANY_LOGO_ALIGN_RIGHT_TOP,
    )
    wide_banner_configs_list.append(wide_banner_configs)

    rom_file_title = "redearth"
    rom_file_title_list.append(rom_file_title)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        game_logo_size=(240, 120),
        game_logo_left_top=(352, 16),
        company_logo_left_top=StandardBannerConfigs.COMPANY_LOGO_ALIGN_LEFT_BOTTOM,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    wide_banner_configs = WideBannerConfigs(rom_file_title)
    wide_banner_configs_list.append(wide_banner_configs)

    rom_file_title = "sfiii"
    rom_file_title_list.append(rom_file_title)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        game_logo_size=(240, 120),
        # 左上
        game_logo_left_top=(-24, 18),
        company_logo_left_top=StandardBannerConfigs.COMPANY_LOGO_ALIGN_RIGHT_BOTTOM,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    wide_banner_configs = WideBannerConfigs(
        rom_file_title,
        game_logo_size=(540, 270),
        # 居中
        game_logo_left_top=(156, 40),
        company_logo_left_top=WideBannerConfigs.COMPANY_LOGO_ALIGN_LEFT_TOP,
    )
    wide_banner_configs_list.append(wide_banner_configs)

    rom_file_title = "sfiii2"
    rom_file_title_list.append(rom_file_title)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        game_logo_size=(240, 120),
        # 左下
        game_logo_left_top=(6, 208),
        company_logo_left_top=StandardBannerConfigs.COMPANY_LOGO_ALIGN_RIGHT_TOP,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    wide_banner_configs = WideBannerConfigs(rom_file_title)
    wide_banner_configs_list.append(wide_banner_configs)

    rom_file_title = "sfiii3"
    # rom_file_title_list.append(rom_file_title)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        company_logo_left_top=StandardBannerConfigs.COMPANY_LOGO_ALIGN_RIGHT_TOP,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    wide_banner_configs = WideBannerConfigs(
        rom_file_title,
        game_logo_size=(400, 200),
        # 靠右居中
        game_logo_left_top=(430, 85),
        company_logo_left_top=WideBannerConfigs.COMPANY_LOGO_ALIGN_RIGHT_TOP,
    )
    wide_banner_configs_list.append(wide_banner_configs)

    for title in rom_file_title_list:
        WiiChannel_Icon(title).make()

    for configs in standard_banner_configs_list:
        StandardBanner(configs).make()

    for configs in wide_banner_configs_list:
        WideBanner(configs).make()

    # WiiChannel_Icon(rom_file_title).make()
    # StandardBanner(standard_banner_configs).make()
    # WideBanner(wide_banner_configs).make()
