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

class ActionSetType(Enum):
    NORMAL = "normal"
    LIMITED = "limited"

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

class MusicVocalType(Enum):
    ORIGINAL_SONG = "original_song"
    SEKAI = "sekai"
    VIRTUAL_SINGER = "virtual_singer"
    ANOTHER_VOCAL = "another_vocal"
    INSTRUMENTAL = "instrumental"
    APRIL_FOOL_2022 = "april_fool_2022"

class DefaultMusicType(Enum):
    ORIGINAL_MUSIC = "original_music"
    SEKAI = "sekai"

class MusicAchievementType(Enum):
    SCORE_RANK = "score_rank"
    COMBO = "combo"

class MusicAssetType(Enum):
    JACKET = "jacket"

class ReleaseConditionType(Enum):
    NONE = "none"
    USER_RANK = "user_rank"
    UNIT_RANK = "unit_rank"
    MASTER_RANK = "master_rank"
    SHOP = "shop"
    CARD_LEVEL = "card_level"
    MUSIC_DIFFICULTY_BETTER_PLAY = "music_difficulty_better_play"
    UNIT_STORY = "unit_story"
    CHARACTER_RANK = "character_rank"
    INHERIT_COMPLETE = "inherit_complete"
    EVENT_POINT = "event_point"
    EVENT_STORY = "event_story"
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

class IngameNoteJudgeType(Enum):
    PERFECT = "perfect"
    GREAT = "great"
    GOOD = "good"
    BAD = "bad"
    MISS = "miss"
    DEAD = "dead"
    AUTO = "auto"

class IngameCutinCharacterType(Enum):
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

class GachaType(Enum):
    CEIL = "ceil"
    NORMAL = "normal"
    BEGINNER = "beginner"
    GIFT = "gift"

class ResourceType(Enum):
    PAID_JEWEL = "paid_jewel"
    COLORFUL_PASS = "colorful_pass"
    LIVE_POINT = "live_point"
    GACHA_TICKET = "gacha_ticket"
    MATERIAL = "material"
    PRACTICE_TICKET = "practice_ticket"
    COIN = "coin"
    COSTUME_3D = "costume_3d"
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

class HeadCostume3dAssetbundleType(Enum):
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

class MaterialExchangeType(Enum):
    NORMAL = "normal"
    BEGINNER = "beginner"

class BillingShopItemType(Enum):
    JEWEL = "jewel"
    VALUE_SET = "value_set"
    COLORFUL_PASS = "colorful_pass"
    LIVE_MISSION_PASS = "live_mission_pass"
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

class BeginnerMissionCategory(Enum):
    NORMAL = "normal"
    SPECIAL = "special"

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
    AREA_ITEM_5_LEVEL = "area_item_5_level"
    CHARACTER_RANK_ALL = "character_rank_all"
    CLEAR_LIVE_DIFFICULTY_ALL = "clear_live_difficulty_all"
    MASTER_FULL_COMBO = "master_full_combo"
    MASTER_FULL_PERFECT = "master_full_perfect"
    CLEAR_LIVE_TARGET_LIFE = "clear_live_target_life"
    CLEAR_LIVE_CONTINUED = "clear_live_continued"
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
    CLEAR_LIVE_SCHOOL_YEAR_2 = "clear_live_school_year_2"
    CLEAR_LIVE_SCHOOL_MIYAMASUZAKA = "clear_live_school_miyamasuzaka"
    CLEAR_LIVE_SCHOOL_KAMIYAMA = "clear_live_school_kamiyama"
    CLEAR_LIVE_MALE = "clear_live_male"
    MULTI_LIVE_MVP = "multi_live_mvp"
    MULTI_LIVE_SUPER_STAR = "multi_live_super_star"
    COLLECT_COSTUME_3D = "collect_costume_3d"
    LIGHT_SOUND_VIRTUAL_LIVE_TOTAL_CHEER_POINT = "light_sound_virtual_live_total_cheer_point"
    IDOL_VIRTUAL_LIVE_TOTAL_CHEER_POINT = "idol_virtual_live_total_cheer_point"
    STREET_VIRTUAL_LIVE_TOTAL_CHEER_POINT = "street_virtual_live_total_cheer_point"
    THEME_PARK_VIRTUAL_LIVE_TOTAL_CHEER_POINT = "theme_park_virtual_live_total_cheer_point"
    SCHOOL_REFUSAL_VIRTUAL_LIVE_TOTAL_CHEER_POINT = "school_refusal_virtual_live_total_cheer_point"
    PIAPRO_VIRTUAL_LIVE_TOTAL_CHEER_POINT = "piapro_virtual_live_total_cheer_point"
    SEND_FRIEND_REQUEST = "send_friend_request"
    MAKE_FRIEND = "make_friend"
    CLEAR_MULTI_LIVE_ALL_FRIEND = "clear_multi_live_all_friend"

class BondsRewardType(Enum):
    RESOURCE = "resource"
    CUT_IN_VOICE = "cut_in_voice"

class VirtualLiveType(Enum):
    BEGINNER = "beginner"
    NORMAL = "normal"
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

class EffectExpressionType(Enum):
    THROW_EFFECT = "throw_effect"

class MessageSize(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    X_LARGE = "x_large"

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

class FacilityType(Enum):
    SKILL_PRACTICE = "skill_practice"
    CHALLENGE_LIVE = "challenge_live"
    RANK_MATCH = "rank_match"

class OneTimeBehaviorType(Enum):
    CHALLENGE_LIVE_CHARACTER_FORCE_RELEASE = "challenge_live_character_force_release"
    VIRTUAL_LIVE_TUTORIAL = "virtual_live_tutorial"

class EventType(Enum):
    MARATHON = "marathon"
    CHEERFUL_CARNIVAL = "cheerful_carnival"

class EventStoryUnitRelation(Enum):
    MAIN = "main"
    SUB = "sub"

class PreliminaryTournamentType(Enum):
    FIRST = "first"
    SECOND = "second"

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

class SkillEffectType(Enum):
    SCORE_UP = "score_up"
    JUDGMENT_UP = "judgment_up"
    LIFE_RECOVERY = "life_recovery"
    SCORE_UP_CONDITION_LIFE = "score_up_condition_life"
    SCORE_UP_KEEP = "score_up_keep"

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

class GachaBehaviorType(Enum):
    ONCE_A_DAY = "once_a_day"
    NORMAL = "normal"
    OVER_RARITY_3_ONCE = "over_rarity_3_once"
    OVER_RARITY_4_ONCE = "over_rarity_4_once"

class GachaPickupType(Enum):
    NORMAL = "normal"

class MissionType(Enum):
    NORMAL_MISSION = "normal_mission"
    BEGINNER_MISSION = "beginner_mission"
    LIVE_MISSION = "live_mission"
    HONOR_MISSION = "honor_mission"

class ResourceBoxPurpose(Enum):
    BILLING_SHOP_ITEM = "billing_shop_item"
    BILLING_SHOP_ITEM_BONUS = "billing_shop_item_bonus"
    BILLING_SHOP_ITEM_COUNT_BONUS = "billing_shop_item_count_bonus"
    BONDS_REWARD = "bonds_reward"
    CARD_EXCHANGE_RESOURCE = "card_exchange_resource"
    CHALLENGE_LIVE_HIGH_SCORE = "challenge_live_high_score"
    CHALLENGE_LIVE_PLAY_DAY_REWARD = "challenge_live_play_day_reward"
    CHALLENGE_LIVE_SCORE_RANK_REWARD_DETAIL = "challenge_live_score_rank_reward_detail"
    CHALLENGE_LIVE_STAGE = "challenge_live_stage"
    CHALLENGE_LIVE_STAGE_EX = "challenge_live_stage_ex"
    CHARACTER_RANK_REWARD = "character_rank_reward"
    CHEERFUL_CARNIVAL_RESULT_REWARD = "cheerful_carnival_result_reward"
    CHEERFUL_CARNIVAL_REWARD = "cheerful_carnival_reward"
    COLORFUL_PASS = "colorful_pass"
    COMPENSATION = "compensation"
    CONNECT_LIVE_REWARD = "connect_live_reward"
    CONVERT_GACHA_CEIL_ITEM = "convert_gacha_ceil_item"
    EPISODE_REWARD = "episode_reward"
    EVENT_EXCHANGE = "event_exchange"
    EVENT_RANKING_REWARD = "event_ranking_reward"
    GACHA_CEIL_EXCHANGE = "gacha_ceil_exchange"
    GACHA_EXTRA = "gacha_extra"
    GIFT_DETAIL = "gift_detail"
    GIFT_GACHA_EXTRA = "gift_gacha_extra"
    LOGIN_BONUS = "login_bonus"
    MASTER_LESSON_REWARD = "master_lesson_reward"
    MATERIAL_EXCHANGE = "material_exchange"
    MISSION_REWARD = "mission_reward"
    MULTI_SCORE_RANK_REWARD_DETAIL = "multi_score_rank_reward_detail"
    MUSIC_ACHIEVEMENT = "music_achievement"
    PLAYER_RANK_REWARD = "player_rank_reward"
    RANK_MATCH_SEASON_TIER_REWARD = "rank_match_season_tier_reward"
    SCORE_RANK_REWARD_DETAIL = "score_rank_reward_detail"
    SHOP_ITEM = "shop_item"
    SUPER_FEVER_REWARD = "super_fever_reward"
    VIRTUAL_LIVE_CHEER_POINT_REWARD = "virtual_live_cheer_point_reward"
    VIRTUAL_LIVE_MEMBER_COUNT_REWARD = "virtual_live_member_count_reward"
    VIRTUAL_LIVE_REWARD = "virtual_live_reward"
    VIRTUAL_SHOP_ITEM = "virtual_shop_item"

class GachaCeilExchangeLabelType(Enum):
    FES = "fes"
    LIMITED = "limited"

class VirtualLiveSetlistType(Enum):
    MC = "mc"
    MUSIC = "music"

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
