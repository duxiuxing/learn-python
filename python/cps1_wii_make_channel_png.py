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

    rom_file_title_filter = None

    rom_file_title = "captcomm"
    rom_file_title_list.append(rom_file_title)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        game_logo_size=(280, 140),
        game_logo_left_top=(278, 134),
        company_logo_left_top=StandardBannerConfigs.COMPANY_LOGO_ALIGN_RIGHT_TOP,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    wide_banner_configs = WideBannerConfigs(
        rom_file_title,
        game_logo_size=(480, 240),
        game_logo_left_top=(175, 110),
        company_logo_left_top=WideBannerConfigs.COMPANY_LOGO_ALIGN_BOTTOM_CENTER,
    )
    wide_banner_configs_list.append(wide_banner_configs)

    rom_file_title = "ffight"
    rom_file_title_list.append(rom_file_title)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        game_logo_size=(420, 210),
        game_logo_left_top=(-32, 72),
        company_logo_left_top=StandardBannerConfigs.COMPANY_LOGO_ALIGN_LEFT_TOP,
        index=1,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        game_logo_size=(300, 150),
        game_logo_left_top=(340, 110),
        company_logo_left_top=StandardBannerConfigs.COMPANY_LOGO_ALIGN_LEFT_BOTTOM,
        index=2,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    wide_banner_configs = WideBannerConfigs(
        rom_file_title,
        company_logo_left_top=WideBannerConfigs.COMPANY_LOGO_ALIGN_RIGHT_TOP,
    )
    wide_banner_configs_list.append(wide_banner_configs)

    rom_file_title = "sf2"
    rom_file_title_list.append(rom_file_title)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        game_logo_size=(340, 170),
        game_logo_left_top=(240, 80),
        company_logo_left_top=StandardBannerConfigs.COMPANY_LOGO_ALIGN_RIGHT_BOTTOM,
        index=1,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        game_logo_size=(220, 110),
        game_logo_left_top=(350, 110),
        company_logo_left_top=StandardBannerConfigs.COMPANY_LOGO_ALIGN_LEFT_BOTTOM,
        index=2,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    wide_banner_configs = WideBannerConfigs(
        rom_file_title,
        game_logo_size=(400, 200),
        game_logo_left_top=(60, 80),
        company_logo_left_top=WideBannerConfigs.COMPANY_LOGO_ALIGN_LEFT_TOP,
    )
    wide_banner_configs_list.append(wide_banner_configs)

    rom_file_title = "sf2ce"
    rom_file_title_list.append(rom_file_title)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        game_logo_size=(340, 170),
        game_logo_left_top=(240, 80),
        company_logo_left_top=StandardBannerConfigs.COMPANY_LOGO_ALIGN_RIGHT_BOTTOM,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    wide_banner_configs = WideBannerConfigs(
        rom_file_title,
        game_logo_size=(400, 200),
        game_logo_left_top=(60, 80),
        company_logo_left_top=WideBannerConfigs.COMPANY_LOGO_ALIGN_LEFT_TOP,
    )
    wide_banner_configs_list.append(wide_banner_configs)

    rom_file_title = "sf2hf"
    rom_file_title_list.append(rom_file_title)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        game_logo_size=(340, 170),
        game_logo_left_top=(240, 80),
        company_logo_left_top=StandardBannerConfigs.COMPANY_LOGO_ALIGN_RIGHT_BOTTOM,
        index=1,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        game_logo_size=(160, 80),
        game_logo_left_top=(400, StandardBannerConfigs.COMPANY_LOGO_OFFSET_Y),
        company_logo_left_top=(23, 16),
        index=2,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    standard_banner_configs = StandardBannerConfigs(
        rom_file_title,
        game_logo_size=(170, 85),
        game_logo_left_top=(8, StandardBannerConfigs.COMPANY_LOGO_OFFSET_Y),
        company_logo_left_top=StandardBannerConfigs.COMPANY_LOGO_ALIGN_RIGHT_BOTTOM,
        index=3,
    )
    standard_banner_configs_list.append(standard_banner_configs)
    wide_banner_configs = WideBannerConfigs(
        rom_file_title,
        game_logo_size=(400, 200),
        game_logo_left_top=(60, 80),
        company_logo_left_top=WideBannerConfigs.COMPANY_LOGO_ALIGN_LEFT_TOP,
    )
    wide_banner_configs_list.append(wide_banner_configs)

    for title in rom_file_title_list:
        if rom_file_title_filter is None:
            WiiChannel_Icon(title).make()
        elif rom_file_title_filter == title:
            WiiChannel_Icon(title).make()

    for configs in standard_banner_configs_list:
        if rom_file_title_filter is None:
            StandardBanner(configs).make()
        elif rom_file_title_filter == configs.rom_file_title:
            StandardBanner(configs).make()

    for configs in wide_banner_configs_list:
        if rom_file_title_filter is None:
            WideBanner(configs).make()
        elif rom_file_title_filter == configs.rom_file_title:
            WideBanner(configs).make()
