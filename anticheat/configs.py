"""MTA Client Anticheat Configs"""

from enum import Enum

class AntiCheatConfigs(Enum):
    """MTA Client Anticheat Configurations"""
    NONE = 0
    HEALTH_ARMOUR_HACK_AC1 = 1
    CORRUPTED_DLL_AC2 = 2
    TRAINER_AC4 = 4
    TRAINER_AC5 = 5
    TRAINER_VF6 = 6
    TRAINER_VF7 = 7
    UNAUTHORIZED_MOD_VF8 = 8
    TRAINERS_AC11 = 11
    DATA_FILE_SD13 = 13
    SPEED_HACK_VF17 = 17
    TRAINER_AC21 = 21
    ANTICHEAT_BLOCK_SD26 = 26

    class SpecialDetection(Enum):
        """MTA Client Special Detection Anticheat"""
        NONE = 0
        DISALLLOW_D3D = 12
        DISALLLOW_VM = 14
        DISALLLOW_DISABLED_DRIVER_SIGN = 15
        DISALLOW_DISABLE_ANTICHEAT = 16
        DISALOW_NON_STANDARD_GTA3 = 20
        DISALLOW_RESOURCE_SCRIPT_DOWNLOAD_ERRORS = 22
        DISALLOW_RESOURCE_FILE_DOWNLOAD_ERRORS = 23
        DISALLOW_WINE = 28
        IGNORE_INJECTED_BY_KEYBOARD_INPUT = 31
        IGNORE_INJECTED_BY_MOUSE_INPUT = 32
        DISALLOW_NET_LIMITERS = 33
        DISALLOW_INTERNET_CAFE = 34
        DISALLOW_FPS_LOCKERS = 35
        DISALLOW_AUTOHOTKEY = 36
