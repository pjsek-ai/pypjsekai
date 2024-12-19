# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from enum import Enum


class Gender(Enum):
    FEMALE = "female"
    MALE = "male"
    SECRET = "secret"


class Figure(Enum):
    LADIES = "ladies"
    MENS = "mens"
    BOYS = "boys"


class BreastSize(Enum):
    M = "m"
    L = "l"
    S = "s"
    NONE = "none"
    SS = "ss"


class Unit(Enum):
    VS = "piapro"
    LN = "light_sound"
    MMJ = "idol"
    VBS = "street"
    WXS = "theme_park"
    NIIGO = "school_refusal"
    NONE = "none"
    ANY = "any"


class SupportUnitType(Enum):
    NONE = "none"
    FULL = "full"
    UNIT = "unit"


class CharacterType(Enum):
    GAME_CHARACTER = "game_character"
    MOB = "mob"
    OUTSIDE_CHARACTER = "outside_character"
    SUB_GAME_CHARACTER = "sub_game_character"


class ActionSetType(Enum):
    NORMAL = "normal"
    LIMITED = "limited"
    MUST_BE_UNIQUE_IN_AREA = "must_be_unique_in_area"


class AreaType(Enum):
    REALITY_WORLD = "reality_world"
    SPIRIT_WORLD = "spirit_world"


class ViewType(Enum):
    SIDE_VIEW = "side_view"
    QUARTER_VIEW = "quarter_view"


class CardRarityType(Enum):
    RARITY_1 = "rarity_1"
    RARITY_2 = "rarity_2"
    RARITY_3 = "rarity_3"
    RARITY_4 = "rarity_4"
    RARITY_BIRTHDAY = "rarity_birthday"


class CardAttr(Enum):
    COOL = "cool"
    HAPPY = "happy"
    MYSTERIOUS = "mysterious"
    CUTE = "cute"
    PURE = "pure"
    ANY = "any"


class ArchiveDisplayType(Enum):
    HIDE = "hide"
    NONE = "none"


class CardParameterType(Enum):
    PARAM1 = "param1"
    PARAM2 = "param2"
    PARAM3 = "param3"


class DescriptionSpriteName(Enum):
    SCORE_UP = "score_up"
    JUDGMENT_UP = "judgment_up"
    LIFE_RECOVERY = "life_recovery"


class CardEpisodePartType(Enum):
    FIRST_PART = "first_part"
    SECOND_PART = "second_part"


class MusicDifficultyType(Enum):
    EASY = "easy"
    NORMAL = "normal"
    HARD = "hard"
    EXPERT = "expert"
    MASTER = "master"
    APPEND = "append"


class MusicVocalType(Enum):
    ORIGINAL_SONG = "original_song"
    SEKAI = "sekai"
    VIRTUAL_SINGER = "virtual_singer"
    ANOTHER_VOCAL = "another_vocal"
    INSTRUMENTAL = "instrumental"
    APRIL_FOOL_2022 = "april_fool_2022"
    STREAMING_LIVE = "streaming_live"


class DefaultMusicType(Enum):
    ORIGINAL_MUSIC = "original_music"
    SEKAI = "sekai"


class MusicAchievementType(Enum):
    SCORE_RANK = "score_rank"
    COMBO = "combo"


class MusicAssetType(Enum):
    JACKET = "jacket"
    MV = "mv"


class ReleaseConditionType(Enum):
    NONE = "none"
    USER_RANK = "user_rank"
    UNIT_RANK = "unit_rank"
    MUSIC_SHOP = "music_shop"
    MASTER_RANK = "master_rank"
    SHOP = "shop"
    PRESENT_RECEIVE = "present_receive"
    CARD_LEVEL = "card_level"
    MUSIC_DIFFICULTY_BETTER_PLAY = "music_difficulty_better_play"
    UNIT_STORY = "unit_story"
    CHARACTER_RANK = "character_rank"
    INHERIT_COMPLETE = "inherit_complete"
    EVENT_POINT = "event_point"
    EVENT_STORY = "event_story"
    WORLD_BLOOM_CHAPTER_START = "world_bloom_chapter_start"
    WORLD_BLOOM_CHAPTER_AGGREGATE = "world_bloom_chapter_aggregate"
    SINCE_EVENT_STARTED = "since_event_started"
    SINCE_EVENT_CLOSED = "since_event_closed"
    SINCE_EVENT_FIRST_VIRTUAL_LIVE_END = "since_event_first_virtual_live_end"
    VIRTUAL_LIVE_PARTICIPATION = "virtual_live_participation"
    RANK_MATCH = "rank_match"
    SPECIAL_STORY = "special_story"
    ACTION_SET = "action_set"
    BONDS_RANK = "bonds_rank"
    CHARACTER_LIVE_USAGE_LEADER = "character_live_usage_leader"
    CHALLENGE_LIVE_CHARACTER_FORCE_RELEASE = "challenge_live_character_force_release"


class LiveType(Enum):
    CHALLENGE_LIVE = "challenge_live"
    CHEERFUL_CARNIVAL_OPEN = "cheerful_carnival_open"
    CHEERFUL_CARNIVAL_PRIVATE = "cheerful_carnival_private"
    MULTI_OPEN = "multi_open"
    PRELIMINARY_TOURNAMENT = "preliminary_tournament"
    RANK_MATCH = "rank_match"
    SOLO = "solo"


class IngameNoteType(Enum):
    NORMAL = "normal"
    LONG = "long"
    LONG_MID = "long_mid"
    LONG_END = "long_end"
    LONG_END_FLICK = "long_end_flick"
    FLICK = "flick"
    NORMAL_CRITICAL = "normal_critical"
    LONG_CRITICAL = "long_critical"
    LONG_MID_CRITICAL = "long_mid_critical"
    LONG_END_CRITICAL = "long_end_critical"
    LONG_END_FLICK_CRITICAL = "long_end_flick_critical"
    FLICK_CRITICAL = "flick_critical"
    LONG_COMBO_AUTO = "long_combo_auto"
    FRICTION = "friction"
    FRICTION_LONG = "friction_long"
    FRICTION_LONG_END = "friction_long_end"
    FRICTION_FLICK = "friction_flick"
    FRICTION_CRITICAL = "friction_critical"
    FRICTION_LONG_CRITICAL = "friction_long_critical"
    FRICTION_LONG_END_CRITICAL = "friction_long_end_critical"
    FRICTION_FLICK_CRITICAL = "friction_flick_critical"


class IngameNoteJudgeType(Enum):
    PERFECT = "perfect"
    GREAT = "great"
    GOOD = "good"
    BAD = "bad"
    MISS = "miss"
    DEAD = "dead"
    AUTO = "auto"


class IngameCutinCharacterType(Enum):
    SP = "sp"
    NORMAL = "normal"
    BONDS = "bonds"


class ShopType(Enum):
    MUSIC = "music"
    LIVE_COSTUME = "live_costume"
    MUSIC_VOCAL = "music_vocal"
    AREA_ITEM = "area_item"
    STAMP = "stamp"


class MaterialType(Enum):
    COMMON = "common"
    COSTUME = "costume"
    MUSIC = "music"
    SPECIAL_TRAINING = "special_training"
    MASTER_LESSON = "master_lesson"
    CARD_TICKET = "card_ticket"
    GACHA_CEIL_TICKET = "gacha_ceil_ticket"
    VOCAL_CARD_TICKET = "vocal_card_ticket"
    CHARACTER_RANK_EXP_TICKET = "character_rank_exp_ticket"
    CARD_EPISODE_RELEASE_TICKET = "card_episode_release_ticket"
    AUTO_EXCHANGE_MUSIC_VOCAL_TICKET = "auto_exchange_music_vocal_ticket"


class GachaType(Enum):
    CEIL = "ceil"
    NORMAL = "normal"
    BEGINNER = "beginner"
    GIFT = "gift"


class ResourceType(Enum):
    AD_REWARD_RANDOM_BOX = "ad_reward_random_box"
    PAID_JEWEL = "paid_jewel"
    COLORFUL_PASS = "colorful_pass"
    LIVE_POINT = "live_point"
    GACHA_TICKET = "gacha_ticket"
    MATERIAL = "material"
    PRACTICE_TICKET = "practice_ticket"
    COIN = "coin"
    COSTUME_3D = "costume_3d"
    COLORFUL_PASS_V2 = "colorful_pass_v2"
    VIRTUAL_COIN = "virtual_coin"
    JEWEL = "jewel"
    SKILL_PRACTICE_TICKET = "skill_practice_ticket"
    BOOST_ITEM = "boost_item"
    BONDS_HONOR = "bonds_honor"
    BONDS_HONOR_WORD = "bonds_honor_word"
    HONOR = "honor"
    AVATAR_COSTUME = "avatar_costume"
    STAMP = "stamp"
    CUSTOM_PROFILE_COLLECTION_RESOURCE = "custom_profile_collection_resource"
    CARD = "card"
    GACHA_CEIL_ITEM = "gacha_ceil_item"
    MUSIC = "music"
    MUSIC_VOCAL = "music_vocal"
    AVATAR_MOTION = "avatar_motion"
    AVATAR_SKIN_COLOR = "avatar_skin_color"
    AVATAR_COORDINATE = "avatar_coordinate"
    CHARACTER_RANK_EXP = "character_rank_exp"
    PAID_VIRTUAL_LIVE = "paid_virtual_live"
    AREA_ITEM = "area_item"
    AVATAR_ACCESSORY = "avatar_accessory"
    PENLIGHT = "penlight"
    VIRTUAL_LIVE_TICKET = "virtual_live_ticket"
    VIRTUAL_LIVE_PAMPHLET = "virtual_live_pamphlet"
    EVENT_ITEM = "event_item"


class LevelType(Enum):
    CARD_SKILL_1 = "card_skill_1"
    CARD_SKILL_2 = "card_skill_2"
    CARD_SKILL_3 = "card_skill_3"
    CARD_SKILL_4 = "card_skill_4"
    CARD = "card"
    USER = "user"
    UNIT = "unit"
    CHARACTER = "character"
    CARD_SKILL_BIRTHDAY = "card_skill_birthday"
    BONDS = "bonds"


class ClientConfigType(Enum):
    INT = "Int"
    FLOAT = "Float"
    STRING = "String"


class Costume3dType(Enum):
    DEFAULT = "default"
    NORMAL = "normal"
    DISTRIBUTION = "distribution"


class PartType(Enum):
    HEAD = "head"
    BODY = "body"
    HAIR = "hair"


class Costume3dRarity(Enum):
    NORMAL = "normal"
    RARE = "rare"


class HeadCostume3dAssetBundleType(Enum):
    HEAD_ONLY = "head_only"
    HEAD_AND_HAIR = "head_and_hair"
    HEAD_ALL = "head_all"
    HEAD_FRONT = "head_front"
    HEAD_BACK = "head_back"


class MotionType(Enum):
    COSTUME_SETTING = "costume_setting"


class TopicType(Enum):
    SPECIAL_STORY_EPISODE = "special_story_episode"
    UNIT_STORY_EPISODE = "unit_story_episode"
    MUSIC_DIFFICULTY = "music_difficulty"
    RULE_SLIDE = "rule_slide"
    VIRTUAL_LIVE_REWARD = "virtual_live_reward"
    CHALLENGE_LIVE = "challenge_live"
    ATTRIBUTE_AREA_ITEM_SHOP = "attribute_area_item_shop"
    FACILITY_CARD_SKILL = "facility_card_skill"
    APP_RATING = "app_rating"
    VIRTUAL_LIVE_TUTORIAL = "virtual_live_tutorial"
    EVENT_STORY_EPISODE = "event_story_episode"
    RANK_MATCH_UNLOCK = "rank_match_unlock"
    INHERIT_COMPLETE = "inherit_complete"
    CUT_IN_VOICE = "cut_in_voice"


class StampType(Enum):
    ILLUSTRATION = "illustration"
    TEXT = "text"
    CHEERFUL_CARNIVAL_MESSAGE = "cheerful_carnival_message"
    NON_CHARACTER_ILLUSTRATION = "non_character_illustration"


class MatchingLogic(Enum):
    RANDOM = "random"
    POWER = "power"


class MultiLiveLobbyType(Enum):
    NORMAL = "normal"
    CHEERFUL_CARNIVAL = "cheerful_carnival"


class RefreshCycle(Enum):
    NONE = "none"
    MONTHLY = "monthly"


class ExchangeCategory(Enum):
    MASTER_PIECE = "master_piece"
    CARD_TICKET = "card_ticket"
    VOCAL_CARD_TICKET = "vocal_card_ticket"
    GACHA_SEAL = "gacha_seal"
    MASTER_CRYSTAL = "master_crystal"
    COMMON_TICKET = "common_ticket"
    CONSUME_MATERIAL = "consume_material"
    HOME_EXCHANGE = "home_exchange"


class MaterialExchangeType(Enum):
    NORMAL = "normal"
    BEGINNER = "beginner"


class BillingShopItemType(Enum):
    JEWEL = "jewel"
    VALUE_SET = "value_set"
    COLORFUL_PASS = "colorful_pass"
    LIVE_MISSION_PASS = "live_mission_pass"
    COLORFUL_PASS_V2 = "colorful_pass_v2"
    COSTUME_3D = "costume_3d"


class BillableLimitType(Enum):
    UNLIMITED = "unlimited"
    COUNT = "count"
    LIVE_POINT = "live_point"


class BillableLimitResetIntervalType(Enum):
    NONE = "none"
    MONTHLY = "monthly"
    DAY = "day"


class PurchaseOption(Enum):
    EXCHANGE = "exchange"


class ColorfulPassTier(Enum):
    TIER_1 = "tier_1"
    TIER_2 = "tier_2"
    TIER_3 = "tier_3"


class JewelBehaviorType(Enum):
    BOOST_RECOVERY = "boost_recovery"


class CharacterMissionType(Enum):
    PLAY_LIVE = "play_live"
    WAITING_ROOM = "waiting_room"
    COLLECT_COSTUME_3D = "collect_costume_3d"
    COLLECT_STAMP = "collect_stamp"
    READ_AREA_TALK = "read_area_talk"
    READ_CARD_EPISODE_FIRST = "read_card_episode_first"
    READ_CARD_EPISODE_SECOND = "read_card_episode_second"
    COLLECT_ANOTHER_VOCAL = "collect_another_vocal"
    AREA_ITEM_LEVEL_UP_CHARACTER = "area_item_level_up_character"
    AREA_ITEM_LEVEL_UP_UNIT = "area_item_level_up_unit"
    AREA_ITEM_LEVEL_UP_REALITY_WORLD = "area_item_level_up_reality_world"
    COLLECT_MEMBER = "collect_member"
    SKILL_LEVEL_UP_RARE = "skill_level_up_rare"
    SKILL_LEVEL_UP_STANDARD = "skill_level_up_standard"
    MASTER_RANK_UP_RARE = "master_rank_up_rare"
    MASTER_RANK_UP_STANDARD = "master_rank_up_standard"
    COLLECT_CHARACTER_ARCHIVE_VOICE = "collect_character_archive_voice"
    PLAY_LIVE_EX = "play_live_ex"
    WAITING_ROOM_EX = "waiting_room_ex"


class NormalMissionType(Enum):
    MAKE_RARE_COSTUME_3D = "make_rare_costume_3d"
    SKILL_LEVEL_2 = "skill_level_2"
    MASTER_RANK = "master_rank"
    MAKE_ANOTHER_COLOR_COSTUME_3D = "make_another_color_costume_3d"
    CHARACTER_RANK_3 = "character_rank_3"
    SET_HONOR = "set_honor"
    CLEAR_LIVE_ANOTHER_VOCAL = "clear_live_another_vocal"
    CLEAR_SOLO_CHALLENGE_LIVE = "clear_solo_challenge_live"
    READ_CHARACTER_PROFILE_EPISODE = "read_character_profile_episode"
    READ_CARD_EPISODE_FIRST = "read_card_episode_first"
    READ_CARD_EPISODE_SECOND = "read_card_episode_second"
    USE_VIRTUAL_ITEM = "use_virtual_item"
    BUY_AVATAR_SKIN = "buy_avatar_skin"
    INHERIT_PLATFORM = "inherit_platform"
    CLEAR_VIRTUAL_LIVE = "clear_virtual_live"
    LIVE_CLEAR = "live_clear"
    MAKE_FRIEND = "make_friend"


class BeginnerMissionType(Enum):
    READ_UNIT_STORY_THEME_PARK = "read_unit_story_theme_park"
    READ_UNIT_STORY_IDOL = "read_unit_story_idol"
    READ_UNIT_STORY_STREET = "read_unit_story_street"
    READ_UNIT_STORY_LIGHT_SOUND = "read_unit_story_light_sound"
    READ_UNIT_STORY_SCHOOL_REFUSAL = "read_unit_story_school_refusal"
    READ_UNIT_STORY_PIAPRO = "read_unit_story_piapro"
    CLEAR_MULTI_LIVE = "clear_multi_live"
    BUY_MUSIC = "buy_music"
    MAKE_COSTUME_3D = "make_costume_3d"
    BUY_AREA_ITEM = "buy_area_item"
    ACHIEVE_BEGINNER_MISSION = "achieve_beginner_mission"

    ANY_LIVE_CLEAR = "any_live_clear"
    MULTI_LIVE_CLEAR = "multi_live_clear"
    EXCHANGE_ANY_MUSIC = "exchange_any_music"
    MAKE_ANY_COSTUME = "make_any_costume"
    CHANGE_ANY_CHARACTER_COSTUME = "change_any_character_costume"
    ANY_CARD_LEVEL_UP = "any_card_level_up"
    READ_BOTH_OF_CARD_STORY = "read_both_of_card_story"
    EXCHANGE_ANY_AREA_ITEM = "exchange_any_area_item"
    JOIN_ANY_VIRTUAL_LIVE = "join_any_virtual_live"
    USE_ANY_VIRTUAL_ITEM = "use_any_virtual_item"
    WATCH_ANY_MUSIC_VIDEO_FULL = "watch_any_music_video_full"
    SET_PROFILE_HONORS_FULL = "set_profile_honors_full"
    CHALLENGE_LIVE_CLEAR = "challenge_live_clear"
    MAKE_NEW_FRIEND = "make_new_friend"
    SET_INHERIT_PLATFORM = "set_inherit_platform"
    READ_UNIT_STORY = "read_unit_story"
    ACHIEVE_ALL_MISSIONS = "achieve_all_missions"


class BeginnerMissionCategory(Enum):
    NORMAL = "normal"
    SPECIAL = "special"
    COMPLETE = "complete"


class ResourceBoxType(Enum):
    EXPAND = "expand"
    COSTUME_3D = "costume_3d"
    LIST = "list"


class LiveMissionType(Enum):
    FREE = "free"
    PREMIUM = "premium"


class LiveTalkType(Enum):
    SUCCESS = "success"
    FAILED = "failed"


class HonorType(Enum):
    CHARACTER = "character"
    ACHIEVEMENT = "achievement"
    EVENT = "event"
    RANK_MATCH = "rank_match"


class HonorRarity(Enum):
    LOW = "low"
    MIDDLE = "middle"
    HIGH = "high"
    HIGHEST = "highest"


class HonorMissionType(Enum):
    CLEAR_LIVE = "clear_live"
    PLAYER_RANK = "player_rank"
    LOGIN_CONTINUED = "login_continued"
    LOGIN_TOTAL = "login_total"
    COLLECT_ANOTHER_VOCAL = "collect_another_vocal"
    UNIT_RANK_ALL = "unit_rank_all"
    READ_UNIT_STORY_NO_SKIP = "read_unit_story_no_skip"
    AREA_ITEM_5_LEVEL = "area_item_5_level"
    CHARACTER_RANK_ALL = "character_rank_all"
    CLEAR_LIVE_DIFFICULTY_ALL = "clear_live_difficulty_all"
    CLEAR_LIVE_TARGET_LIFE = "clear_live_target_life"
    CLEAR_LIVE_CONTINUED = "clear_live_continued"
    FINISH_LIVE_WITH_EMPTY_LIFE = "finish_live_with_empty_life"
    CLEAR_LIVE_COMBO = "clear_live_combo"
    COLLECT_COIN_TOTAL = "collect_coin_total"
    CLEAR_MULTI_LIVE_FULL_COMBO_ALL = "clear_multi_live_full_combo_all"
    MULTI_LIVE_SELECT_SAME_MUSIC = "multi_live_select_same_music"
    MULTI_LIVE_SAME_HONOR = "multi_live_same_honor"
    MULTI_LIVE_STAMP = "multi_live_stamp"
    DUPLICATE_CARD_TOTAL = "duplicate_card_total"
    COLLECT_STAMP = "collect_stamp"
    ACTION_SET = "action_set"
    READ_STORY_NO_SKIP = "read_story_no_skip"
    CLEAR_LIVE_SCHOOL_YEAR_1 = "clear_live_school_year_1"
    CLEAR_LIVE_NEXT_GRADE_SCHOOL_YEAR_2 = "clear_live_next_grade_school_year_2"
    CLEAR_LIVE_SCHOOL_YEAR_2 = "clear_live_school_year_2"
    CLEAR_LIVE_NEXT_GRADE_SCHOOL_YEAR_3 = "clear_live_next_grade_school_year_3"
    CLEAR_LIVE_SCHOOL_MIYAMASUZAKA = "clear_live_school_miyamasuzaka"
    CLEAR_LIVE_SCHOOL_KAMIYAMA = "clear_live_school_kamiyama"
    CLEAR_LIVE_MALE = "clear_live_male"
    MULTI_LIVE_MVP = "multi_live_mvp"
    MULTI_LIVE_SUPER_STAR = "multi_live_super_star"
    COLLECT_COSTUME_3D = "collect_costume_3d"
    CHEER_POINT_RANK_1ST = "cheer_point_rank_1st"
    CHEER_POINT_RANK_10TH = "cheer_point_rank_10th"
    LIGHT_SOUND_VIRTUAL_LIVE_TOTAL_CHEER_POINT = "light_sound_virtual_live_total_cheer_point"
    IDOL_VIRTUAL_LIVE_TOTAL_CHEER_POINT = "idol_virtual_live_total_cheer_point"
    STREET_VIRTUAL_LIVE_TOTAL_CHEER_POINT = "street_virtual_live_total_cheer_point"
    THEME_PARK_VIRTUAL_LIVE_TOTAL_CHEER_POINT = "theme_park_virtual_live_total_cheer_point"
    SCHOOL_REFUSAL_VIRTUAL_LIVE_TOTAL_CHEER_POINT = "school_refusal_virtual_live_total_cheer_point"
    PIAPRO_VIRTUAL_LIVE_TOTAL_CHEER_POINT = "piapro_virtual_live_total_cheer_point"
    SEND_FRIEND_REQUEST = "send_friend_request"
    MAKE_FRIEND = "make_friend"
    CLEAR_MULTI_LIVE_ALL_FRIEND = "clear_multi_live_all_friend"
    EASY_FULL_COMBO = "easy_full_combo"
    EASY_FULL_PERFECT = "easy_full_perfect"
    NORMAL_FULL_COMBO = "normal_full_combo"
    NORMAL_FULL_PERFECT = "normal_full_perfect"
    HARD_FULL_COMBO = "hard_full_combo"
    HARD_FULL_PERFECT = "hard_full_perfect"
    EXPERT_FULL_COMBO = "expert_full_combo"
    EXPERT_FULL_PERFECT = "expert_full_perfect"
    MASTER_FULL_COMBO = "master_full_combo"
    MASTER_FULL_PERFECT = "master_full_perfect"
    APPEND_FULL_COMBO = "append_full_combo"
    APPEND_FULL_PERFECT = "append_full_perfect"
    PLAY_LEVEL_CLEAR = "play_level_clear"
    PLAY_LEVEL_FULL_COMBO_CLEAR = "play_level_full_combo_clear"


class BondsRewardType(Enum):
    RESOURCE = "resource"
    CUT_IN_VOICE = "cut_in_voice"


class VirtualLiveType(Enum):
    BEGINNER = "beginner"
    NORMAL = "normal"
    PAID = "paid"
    ARCHIVE = "archive"
    CHEERFUL_CARNIVAL = "cheerful_carnival"
    STREAMING = "streaming"


class VirtualShopType(Enum):
    OTHER = "other"
    EVENT = "event"
    BIRTHDAY = "birthday"
    SPECIAL_LIVE = "special_live"
    VIRTUAL_LIVE_TICKET = "virtual_live_ticket"


class VirtualItemCategory(Enum):
    NORMAL = "normal"
    SPREAD = "spread"


class PaidVirtualLiveShopItemPurchaseType(Enum):
    SINGLE = "single"
    BUNDLE = "bundle"


class PaidVirtualLiveType(Enum):
    STREAMING = "streaming"
    BIRTHDAY = "birthday"
    SEASON = "season"
    WELCOME = "welcome"


class EffectExpressionType(Enum):
    THROW_EFFECT = "throw_effect"


class MessageSize(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    X_LARGE = "x_large"
    XX_LARGE = "xx_large"


class VirtualLiveTicketType(Enum):
    PAID = "paid"


class RuleSlideType(Enum):
    MUSIC_SHOP = "MUSIC_SHOP"
    WORLD_MAP = "WORLD_MAP"
    MULTI_LIVE = "MULTI_LIVE"
    COSTUME_CHANGE = "COSTUME_CHANGE"
    COSTUME_CHANGE_MIKU = "COSTUME_CHANGE_MIKU"
    AREA_SHOP_SEKAI = "AREA_SHOP_SEKAI"
    VIRTUAL_LIVE_OVERVIEW = "VIRTUAL_LIVE_OVERVIEW"
    VIRTUAL_WAITING_ROOM = "VIRTUAL_WAITING_ROOM"
    VIRTUAL_IN_LIVE = "VIRTUAL_IN_LIVE"
    COSTUME_SHOP = "COSTUME_SHOP"
    CHARACTER_RANK = "CHARACTER_RANK"
    CHALLENGE_LIVE_CHARACTER_SELECT = "CHALLENGE_LIVE_CHARACTER_SELECT"
    CHALLENGE_LIVE_CHARACTER_ADD = "CHALLENGE_LIVE_CHARACTER_ADD"
    SKILL_UP = "SKILL_UP"
    STAMP_SHOP = "STAMP_SHOP"
    MASTER_TRAINING = "MASTER_TRAINING"
    ANOTHER_VOCAL_SHOP = "ANOTHER_VOCAL_SHOP"
    WAITING_ROOM = "WAITING_ROOM"
    FREE_STAMP = "FREE_STAMP"
    AREA_SHOP_SCHOOL = "AREA_SHOP_SCHOOL"
    MISSION = "MISSION"
    SUMMARY = "SUMMARY"
    CHALLENGE_LIVE = "CHALLENGE_LIVE"
    FREE_LIVE = "FREE_LIVE"
    LESSON = "LESSON"
    SPECIAL_TRAINING = "SPECIAL_TRAINING"
    LIVE_BONUS = "LIVE_BONUS"
    EVENT_TOP = "EVENT_TOP"
    EVENT_DECK = "EVENT_DECK"
    GUILD_VIRTUAL_LIVE_TOP = "GUILD_VIRTUAL_LIVE_TOP"
    AUTO_LIVE = "AUTO_LIVE"
    VIRTUAL_LIVE_MESSAGE = "VIRTUAL_LIVE_MESSAGE"
    GACHA_ITEM = "GACHA_ITEM"
    STORY_EVENT = "STORY_EVENT"
    FRIEND_LIST = "FRIEND_LIST"
    SELECT_LIST = "SELECT_LIST"
    CHEERFUL_CARNIVAL = "CHEERFUL_CARNIVAL"
    GACHA_BONUS = "GACHA_BONUS"
    CHANGEROOM_MEMBER = "CHANGEROOM_MEMBER"
    CUSTOM_PROFILE = "CUSTOM_PROFILE"
    PIAPRO_BONUS = "PIAPRO_BONUS"
    BONDS = "BONDS"
    RANK_MATCH = "RANK_MATCH"
    GIFT_GACHA = "GIFT_GACHA"
    COLORFUL_SELECT_LIST = "COLORFUL_SELECT_LIST"
    STAMP_MISSION = "STAMP_MISSION"
    MYLIST = "MYLIST"
    STAMP_MISSION_3RD_ANNIV = "STAMP_MISSION_3RD_ANNIV"
    WORLD_MAP_V2 = "WORLD_MAP_V2"
    GACHA_RECOLLECTION_SELECT = "GACHA_RECOLLECTION_SELECT"
    COLORFUL_SELECT_AND_FORTUNE_FLOWER = "COLORFUL_SELECT_AND_FORTUNE_FLOWER"


class FacilityType(Enum):
    SKILL_PRACTICE = "skill_practice"
    CHALLENGE_LIVE = "challenge_live"
    RANK_MATCH = "rank_match"


class OneTimeBehaviorType(Enum):
    CHALLENGE_LIVE_CHARACTER_FORCE_RELEASE = "challenge_live_character_force_release"
    VIRTUAL_LIVE_TUTORIAL = "virtual_live_tutorial"
    WORLD_BLOOM_AREA_UNLOCK_LIGHT_SOUND = "world_bloom_area_unlock_light_sound"
    WORLD_BLOOM_AREA_UNLOCK_IDOL = "world_bloom_area_unlock_idol"
    WORLD_BLOOM_AREA_UNLOCK_STREET = "world_bloom_area_unlock_street"
    WORLD_BLOOM_AREA_UNLOCK_THEME_PARK = "world_bloom_area_unlock_theme_park"
    WORLD_BLOOM_AREA_UNLOCK_SCHOOL_REFUSAL = "world_bloom_area_unlock_school_refusal"


class EventType(Enum):
    MARATHON = "marathon"
    CHEERFUL_CARNIVAL = "cheerful_carnival"
    WORLD_BLOOM = "world_bloom"


class EventStoryUnitRelation(Enum):
    MAIN = "main"
    SUB = "sub"


class PreliminaryTournamentType(Enum):
    FIRST = "first"
    SECOND = "second"
    THIRD = "third"
    FOURTH = "fourth"
    FIFTH = "fifth"
    SIXTH = "sixth"


class CheerfulCarnivalTeamPointTermType(Enum):
    CHEERFUL_CARNIVAL_TEAM_POINT_1ST = "cheerful_carnival_team_point_1st"
    CHEERFUL_CARNIVAL_TEAM_POINT_2ND = "cheerful_carnival_team_point_2nd"
    CHEERFUL_CARNIVAL_TEAM_POINT_FINAL = "cheerful_carnival_team_point_final"


class CheerfulCarnivalResultType(Enum):
    VICTORY = "victory"
    DEFEAT = "defeat"
    DRAW = "draw"


class AppealTargetType(Enum):
    GACHA = "gacha"


class AppealType(Enum):
    ONCE = "once"


class AppealReadConditionType(Enum):
    TRANSITION = "transition"


class StoryType(Enum):
    UNIT_STORY = "unit_story"
    EVENT_STORY = "event_story"
    CARD_STORY = "card_story"
    SPECIAL_STORY = "special_story"


class CustomProfileResourceType(Enum):
    PLAYER_INFO = "player_info"
    GENERAL_BACKGROUND = "general_background"
    STORY_BACKGROUND = "story_background"
    COLLECTION = "collection"
    MEMBER_STANDING_PICTURE = "member_standing_picture"
    SHAPE = "shape"
    ETC = "etc"


class ResourceLoadType(Enum):
    PREFAB = "prefab"
    ASSETBUNDLE = "assetbundle"


class CustomProfileResourceCollectionType(Enum):
    OMIKUJI = "omikuji"
    CAN_BADGE = "can_badge"


class FortuneType(Enum):
    GRATE_FORTUNE = "grate_fortune"
    FORTUNE = "fortune"
    MIDDLE_FORTUNE = "middle_fortune"
    SMALL_FORTUNE = "small_fortune"
    UNCERTAIN_LUCK = "uncertain_luck"
    MISFORTUNE = "misfortune"
    GRATE_MISFORTUNE = "grate_misfortune"


class VirtualBoothShopType(Enum):
    VIRTUAL_SHOP = "virtual_shop"
    OMIKUJI = "omikuji"
    COLLECTION_GACHA = "collection_gacha"


class SpecialSeasonAreaUseType(Enum):
    BGM = "bgm"
    AREA = "area"


class RankMatchPenaltyType(Enum):
    WARNING_POP = "warning_pop"
    MINUTES_BAN = "minutes_ban"
    HOURS_BAN = "hours_ban"
    SEASON_BAN = "season_ban"


class RankMatchPlacementConditionType(Enum):
    ALL_PERFECT = "all_perfect"
    ALL_WIN = "all_win"
    ALL_LOSE = "all_lose"
    LIFE_0 = "life_0"


class TierBehaviorType(Enum):
    CLASS_UP = "class_up"
    CLASS_DOWN = "class_down"


class RankMatchBonusPointConditionType(Enum):
    ALL_PERFECT = "all_perfect"
    FULL_COMBO = "full_combo"
    HIGHER_CLASS_WIN = "higher_class_win"
    LIFE_0 = "life_0"


class CalcType(Enum):
    ADD = "add"
    SUBTRACT = "subtract"


class ActivateEffectValueType(Enum):
    RATE = "rate"
    FIXED = "fixed"
    REFERENCE_RATE = "reference_rate"


class SkillEffectType(Enum):
    SCORE_UP = "score_up"
    JUDGMENT_UP = "judgment_up"
    LIFE_RECOVERY = "life_recovery"
    SCORE_UP_CONDITION_LIFE = "score_up_condition_life"
    SCORE_UP_KEEP = "score_up_keep"
    SCORE_UP_CHARACTER_RANK = "score_up_character_rank"
    OTHER_MEMBER_SCORE_UP_REFERENCE_RATE = "other_member_score_up_reference_rate"
    SCORE_UP_UNIT_COUNT = "score_up_unit_count"


class SkillEffectConditionType(Enum):
    EQUALS_OR_OVER = "equals_or_over"


class SkillEnhanceType(Enum):
    SUB_UNIT_SCORE_UP = "sub_unit_score_up"


class MusicCategory(Enum):
    MV = "mv"
    MV_2D = "mv_2d"
    IMAGE = "image"
    ORIGINAL = "original"


class LotteryType(Enum):
    NORMAL = "normal"
    CATEGORIZED_WISH = "categorized_wish"


class GachaDetailWishType(Enum):
    NORMAL = "normal"
    LIMITED = "limited"
    FIXED = "fixed"


class GachaBehaviorType(Enum):
    ONCE_A_DAY = "once_a_day"
    NORMAL = "normal"
    OVER_RARITY_3_ONCE = "over_rarity_3_once"
    OVER_RARITY_4_ONCE = "over_rarity_4_once"
    ONCE_A_WEEK = "once_a_week"


class ResourceCategory(Enum):
    CONSUME_RESOURCE = "consume_resource"
    FREE_RESOURCE = "free_resource"


class GachaSpinnableType(Enum):
    ANY = "any"
    COLORFUL_PASS = "colorful_pass"


class GachaPickupType(Enum):
    NORMAL = "normal"


class MissionType(Enum):
    NORMAL_MISSION = "normal_mission"
    BEGINNER_MISSION = "beginner_mission"
    LIVE_MISSION = "live_mission"
    HONOR_MISSION = "honor_mission"
    EVENT_MISSION = "event_mission"
    PANEL_MISSION = "panel_mission"
    PANEL_MISSION_COMPLETE = "panel_mission_complete"
    BEGINNER_MISSION_V2 = "beginner_mission_v2"


class ResourceBoxPurpose(Enum):
    AD_REWARD = "ad_reward"
    AD_REWARD_RANDOM_BOX = "ad_reward_random_box"
    BILLING_SHOP_ITEM = "billing_shop_item"
    BILLING_SHOP_ITEM_BONUS = "billing_shop_item_bonus"
    BILLING_SHOP_ITEM_COUNT_BONUS = "billing_shop_item_count_bonus"
    BILLING_SHOP_ITEM_ZENPAY_BONUS = "billing_shop_item_zenpay_bonus"
    BONDS_REWARD = "bonds_reward"
    CARD_EXCHANGE_RESOURCE = "card_exchange_resource"
    CARD_EXTRA = "card_extra"
    CHALLENGE_LIVE_HIGH_SCORE = "challenge_live_high_score"
    CHALLENGE_LIVE_PLAY_DAY_REWARD = "challenge_live_play_day_reward"
    CHALLENGE_LIVE_SCORE_RANK_REWARD_DETAIL = "challenge_live_score_rank_reward_detail"
    CHALLENGE_LIVE_STAGE = "challenge_live_stage"
    CHALLENGE_LIVE_STAGE_EX = "challenge_live_stage_ex"
    CHARACTER_RANK_REWARD = "character_rank_reward"
    CHEERFUL_CARNIVAL_RESULT_REWARD = "cheerful_carnival_result_reward"
    CHEERFUL_CARNIVAL_REWARD = "cheerful_carnival_reward"
    COLORFUL_PASS = "colorful_pass"
    COLORFUL_PASS_V2 = "colorful_pass_v2"
    COMPENSATION = "compensation"
    CONNECT_LIVE_REWARD = "connect_live_reward"
    CONVERT_GACHA_CEIL_ITEM = "convert_gacha_ceil_item"
    EPISODE_REWARD = "episode_reward"
    EVENT_EXCHANGE = "event_exchange"
    EVENT_MISSION_SELECTABLE_REWARD = "event_mission_selectable_reward"
    EVENT_RANKING_REWARD = "event_ranking_reward"
    FRIEND_INVITATION_CAMPAIGN_MISSION_REWARD = "friend_invitation_campaign_mission_reward"
    GACHA_BONUS_ITEM_RECEIVABLE_REWARD = "gacha_bonus_item_receivable_reward"
    GACHA_CEIL_EXCHANGE = "gacha_ceil_exchange"
    GACHA_EXTRA = "gacha_extra"
    GACHA_FREEBIE_GROUP = "gacha_freebie_group"
    GIFT_DETAIL = "gift_detail"
    GIFT_GACHA_EXTRA = "gift_gacha_extra"
    LOGIN_BONUS = "login_bonus"
    MASTER_LESSON_REWARD = "master_lesson_reward"
    MATERIAL_EXCHANGE = "material_exchange"
    MATERIAL_EXCHANGE_FREEBIE = "material_exchange_freebie"
    MISSION_REWARD = "mission_reward"
    MULTI_SCORE_RANK_REWARD_DETAIL = "multi_score_rank_reward_detail"
    MUSIC_ACHIEVEMENT = "music_achievement"
    PAID_VIRTUAL_LIVE_SHOP_ITEM = "paid_virtual_live_shop_item"
    PLAYER_RANK_REWARD = "player_rank_reward"
    RANK_MATCH_SCORE_RANK_REWARD_DETAIL = "rank_match_score_rank_reward_detail"
    RANK_MATCH_SEASON_TIER_REWARD = "rank_match_season_tier_reward"
    SCORE_RANK_REWARD_DETAIL = "score_rank_reward_detail"
    SHOP_ITEM = "shop_item"
    STORY_MISSION = "story_mission"
    SUPER_FEVER_REWARD = "super_fever_reward"
    VIRTUAL_LIVE_CHEER_POINT_REWARD = "virtual_live_cheer_point_reward"
    VIRTUAL_LIVE_MEMBER_COUNT_REWARD = "virtual_live_member_count_reward"
    VIRTUAL_LIVE_REWARD = "virtual_live_reward"
    VIRTUAL_SHOP_ITEM = "virtual_shop_item"
    WORLD_BLOOM_CHAPTER_RANKING_REWARD = "world_bloom_chapter_ranking_reward"


class GachaCeilExchangeLabelType(Enum):
    FES = "fes"
    LIMITED = "limited"


class VirtualLiveSetlistType(Enum):
    MC = "mc"
    MUSIC = "music"
    MC_TIMELINE = "mc_timeline"


class DayOfWeek(Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"


class VirtualItemLabelType(Enum):
    SPECIAL = "special"


class VirtualLiveStageStatus(Enum):
    OPEN = "open"
    LIVE = "live"


class VirtualShopItemType(Enum):
    AVATAR_MOTION = "avatar_motion"
    COSTUME = "costume"
    ACCESSORY = "accessory"
    COORDINATE = "coordinate"
    PENLIGHT = "penlight"
    VIRTUAL_LIVE_TICKET = "virtual_live_ticket"
    BOOST_ITEM = "boost_item"
    PREMIUM_VIRTUAL_LIVE_TICKET = "premium_virtual_live_ticket"


class AccessoryPart(Enum):
    ACCESSORY_FACE = "Accessory_face"


class SpecialSeasonType(Enum):
    APRIL_FOOL_2022 = "april_fool_2022"


class AppVersionStatus(Enum):
    NOT_AVAILABLE = "not_available"
    AVAILABLE = "available"
    MAINTENANCE = "maintenance"


class BundleCategory(Enum):
    STARTAPP = "StartApp"
    ONDEMAND = "OnDemand"
    ADDITIONALVOICE = "AdditionalVoice"
    TUTORIAL = "Tutorial"


class PanelMissionType(Enum):
    UNIT_LIVE_CLEAR = "unit_live_clear"
    UNIT_AVATAR_JOIN_VIRTUAL_LIVE = "unit_avatar_join_virtual_live"
    UNIT_LIVE_CLEAR_MUSIC = "unit_live_clear_music"
    UNIT_LIVE_CLEAR_ANOTHER_VOCAL = "unit_live_clear_another_vocal"
    UNIT_MULTI_LIVE_CLEAR_HONOR = "unit_multi_live_clear_honor"
    UNIT_COLLECT_COSTUME_3D = "unit_collect_costume_3d"
    UNIT_COLLECT_CARD = "unit_collect_card"
    MULTI_LIVE_CLEAR = "multi_live_clear"
    CARD_LEVEL_UP = "card_level_up"
    READ_EVENT_STORY_EPISODE = "read_event_story_episode"
    JOIN_VIRTUAL_LIVE = "join_virtual_live"
    SET_VIRTUAL_LIVE_AVATAR_MOTION = "set_virtual_live_avatar_motion"
    MAKE_NEW_FRIEND = "make_new_friend"
    EXECUTE_GACHA = "execute_gacha"
    MULTI_LIVE_CLEAR_MUSIC_WITH_FRIENDS = "multi_live_clear_music_with_friends"
    MULTI_LIVE_CLEAR_PARTY_FULL_COMBO = "multi_live_clear_party_full_combo"
    MULTI_LIVE_CLEAR_SUPER_FEVER = "multi_live_clear_super_fever"
    LIVE_CLEAR_AM_PM = "live_clear_am_pm"
    MULTI_LIVE_CLEAR_TOP_SCORE = "multi_live_clear_top_score"
    COLLECT_EVENT_POINT = "collect_event_point"
    GET_LIVE_PERFECT = "get_live_perfect"
    MULTI_LIVE_CLEAR_MUSIC_SCORE = "multi_live_clear_music_score"
    SPIN_GACHA = "spin_gacha"
    EXECUTE_GACHA_TAB = "execute_gacha_tab"
    PURCHASE_BILLING_SHOP_ITEM_IN_CATEGORY = "purchase_billing_shop_item_in_category"
    PURCHASE_PREMIUM_MISSION_PASS = "purchase_premium_mission_pass"
    COLLECT_VIRTUAL_LIVE_CHEER_POINT = "collect_virtual_live_cheer_point"
    SPIN_CUSTOM_PROFILE_GACHA_TAB = "spin_custom_profile_gacha_tab"
    LIVE_CLEAR_FULL_COMBO = "live_clear_full_combo"
    LIVE_CLEAR_SKILL_SCORE_UP = "live_clear_skill_score_up"
    LIVE_CLEAR_SKILL_JUDGEMENT_UP = "live_clear_skill_judgement_up"
    LIVE_CLEAR_SKILL_LIFE_RECOVERY = "live_clear_skill_life_recovery"
    ANY_MEMBER_SKILL_UP = "any_member_skill_up"
    COLLECT_MATERIAL = "collect_material"
    LIVE_CLEAR_IN_MUSIC_GROUP = "live_clear_in_music_group"
    LIVE_CLEAR_FULL_COMBO_IN_MUSIC_LEVEL = "live_clear_full_combo_in_music_level"
    LIVE_CLEAR_IN_MUSIC_LEVEL = "live_clear_in_music_level"
    LIVE_CLEAR_ALL_PERFECT_IN_MUSIC_DIFFICULTY = "live_clear_all_perfect_in_music_difficulty"
    LIVE_CLEAR_RANK_MATCH = "live_clear_rank_match"
    LIVE_CLEAR_FULL_COMBO_ALL_DIFFICULTY_IN_MUSIC = "live_clear_full_combo_all_difficulty_in_music"
    LIVE_CLEAR_ALL_PERFECT_ALL_DIFFICULTY_IN_MUSIC = "live_clear_all_perfect_all_difficulty_in_music"
    LIVE_CLEAR_IN_MUSIC = "live_clear_in_music"
    MULTI_LIVE_CLEAR_WITH_FRIENDS = "multi_live_clear_with_friends"
    LIVE_CLEAR_WITH_MIRROR = "live_clear_with_mirror"
    LIVE_CLEAR_WITH_MV_2D_OR_ORIGINAL = "live_clear_with_mv_2d_or_original"
    LIVE_CLEAR_WITH_MV_3D = "live_clear_with_mv_3d"
    LIVE_CLEAR_NO_CONTINUE_IN_MUSIC_AND_DIFFICULTY = "live_clear_no_continue_in_music_and_difficulty"
    LOGIN = "login"
    LIVE_CLEAR_WITH_DIFFERENT_MUSIC = "live_clear_with_different_music"
    LIVE_CLEAR = "live_clear"
    READ_UNIT_OR_EVENT_OR_CARD_STORY_EPISODE = "read_unit_or_event_or_card_story_episode"
    SPIN_ANY_GACHA = "spin_any_gacha"
    REPLAY_ANY_MV = "replay_any_mv"
    PLAY_LIVE_WITH_UNIT = "play_live_with_unit"
    CONSUME_BOOST_COUNT = "consume_boost_count"
    READ_EVENT_LINKED_CARD_EPISODE_WITHOUT_SKIP = "read_event_linked_card_episode_without_skip"
    READ_ALL_EVENT_STORY_EPISODE_WITHOUT_SKIP = "read_all_event_story_episode_without_skip"
    COLLECT_VIRTUAL_LIVE_CHEER_POINT_IN_LIVE = "collect_virtual_live_cheer_point_in_live"
    BONDS_RANK_UP = "bonds_rank_up"


class EventMissionType(Enum):
    LIVE_CLEAR_DAILY = "live_clear_daily"
    ANY_LIVE_CLEAR = "any_live_clear"
    LIVE_CLEAR_FULL_COMBO = "live_clear_full_combo"
    LIVE_CLEAR_DIFFERENT_MUSIC = "live_clear_different_music"
    READ_LAST_EVENT_STORY_EPISODE = "read_last_event_story_episode"
    CONSUME_EVENT_ITEM = "consume_event_item"
    JOIN_VIRTUAL_LIVE = "join_virtual_live"
    ACHIEVE_EVENT_MISSION = "achieve_event_mission"


class EventMissionCategory(Enum):
    NORMAL = "normal"
    COMPLETE = "complete"
    COMPLETE_SELECTABLE_REWARD = "complete_selectable_reward"


class RankingViewType(Enum):
    TOP100 = "top100"
    USER_MYSELF = "user_myself"
    NEAR_USER = "near_user"


class DisplayTimelineType(Enum):
    ALL = "all"
    NEXT_GRADE = "next_grade"


class GachaDisplayType(Enum):
    ALWAYS = "always"
    HAVING = "having"


class WorldBloomSupportDeckCharacterType(Enum):
    SPECIFIC = "specific"
    OTHERS = "others"


class FriendInvitationCampaignMissionType(Enum):
    HOST = "host"
    GUEST = "guest"


class AdditionalAreaType(Enum):
    NONE = "none"
    COLLABORATION = "collaboration"
    APRIL_FOOL = "april_fool"


class CharacterArchiveVoiceType(Enum):
    LIVE_CUTIN_NORMAL = "live_cutin_normal"
    LIVE_CUTIN_PAIR = "live_cutin_pair"
    LIVE_RESULT = "live_result"
    COMMENT_LIVE_TOP = "comment_live_top"
    COMMENT_LOGIN_BONUS = "comment_login_bonus"
    PRACTICE = "practice"
    COLLECT_CARD = "collect_card"


class CharacterArchiveVoiceTagType(Enum):
    LIVE_CUTIN = "live_cutin"
    LIVE_RESULT = "live_result"
    BIRTHDAY = "birthday"
    SEASON = "season"
    NORMAL = "normal"


class LiveClearVoiceType(Enum):
    RANK_D = "rank_d"
    OVER_RANK_C = "over_rank_c"
    FULL_COMBO = "full_combo"
    FULL_PERFECT = "full_perfect"

class AdRewardPlayType(Enum):
    BILLING_SHOP_FOR_JEWEL = "billing_shop_for_jewel"
    PRESENT_BOX = "present_box"
    EVENT_EXCHANGE = "event_exchange"
    BOOST = "boost"
    LIVE_MISSION = "live_mission"
    MUSIC_SHOP = "music_shop"


class VirtualLivePerformanceType(Enum):
    MAIN_ONLY = "main_only"
    BOTH = "both"


class CardSupplyType(Enum):
    NORMAL = "normal"
    BIRTHDAY = "birthday"
    TERM_LIMITED = "term_limited"
    COLORFUL_FESTIVAL_LIMITED = "colorful_festival_limited"
    BLOOM_FESTIVAL_LIMITED = "bloom_festival_limited"
    UNIT_EVENT_LIMITED = "unit_event_limited"
    COLLABORATION_LIMITED = "collaboration_limited"


class MaterialExchangeFreebieType(Enum):
    EXCHANGE_ALREADY_OWNED_CARD = "exchange_already_owned_card"


class GachaBonusRewardType(Enum):
    ITEM = "item"
    NOT_OWNED_RANDOM_RARITY4_FIXED = "not_owned_random_rarity4_fixed"
    SELECTABLE_RARITY4_FIXED = "selectable_rarity4_fixed"


class BillingPlatform(Enum):
    ANDROID = "Android"
    IOS = "iOS"
    ZENPAY = "zenpay"