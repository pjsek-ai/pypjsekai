# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from typing import List, Optional, Union

from pjsekai.enums import *
from .model import Model


class GameCharacter(Model):
    id: Optional[int]
    seq: Optional[int]
    resource_id: Optional[int]
    first_name: Optional[str]
    given_name: Optional[str]
    first_name_ruby: Optional[str]
    given_name_ruby: Optional[str]
    gender: Optional[Union[Gender, Unknown]]
    height: Optional[float]
    live2d_height_adjustment: Optional[float]
    figure: Optional[Union[Figure, Unknown]]
    breast_size: Optional[Union[BreastSize, Unknown]]
    model_name: Optional[str]
    unit: Optional[Union[Unit, Unknown]]
    support_unit_type: Optional[Union[SupportUnitType, Unknown]]


class GameCharacterUnit(Model):
    id: Optional[int]
    game_character_id: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    color_code: Optional[str]
    skin_color_code: Optional[str]
    skin_shadow_color_code1: Optional[str]
    skin_shadow_color_code2: Optional[str]


class OutsideCharacter(Model):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]


class Character3d(Model):
    id: Optional[int]
    character_type: Optional[Union[CharacterType, Unknown]]
    character_id: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    name: Optional[str]
    head_costume3d_id: Optional[int]
    hair_costume3d_id: Optional[int]
    body_costume3d_id: Optional[int]


class Character2d(Model):
    id: Optional[int]
    character_type: Optional[Union[CharacterType, Unknown]]
    character_id: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    asset_name: Optional[str]


class CharacterProfile(Model):
    character_id: Optional[int]
    character_voice: Optional[str]
    birthday: Optional[str]
    height: Optional[str]
    school: Optional[str]
    school_year: Optional[str]
    hobby: Optional[str]
    special_skill: Optional[str]
    favorite_food: Optional[str]
    hated_food: Optional[str]
    weak: Optional[str]
    introduction: Optional[str]
    scenario_id: Optional[str]


class Bond(Model):
    id: Optional[int]
    group_id: Optional[int]
    character_id1: Optional[int]
    character_id2: Optional[int]


class Live2d(Model):
    id: Optional[int]
    character_id: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    asset_bundle_name: Optional[str]
    motion: Optional[str]
    expression: Optional[str]
    weight: Optional[int]


class BondsLive2d(Live2d):
    default_flg: Optional[bool]


class BondsRankUpLive2d(Live2d):
    default_flg: Optional[bool]


class UnitProfile(Model):
    unit: Optional[Union[Unit, Unknown]]
    unit_name: Optional[str]
    seq: Optional[int]
    profile_sentence: Optional[str]
    color_code: Optional[str]


class ActionSet(Model):
    id: Optional[int]
    area_id: Optional[int]
    script_id: Optional[str]
    character_ids: Optional[List[int]]
    archive_display_type: Optional[Union[ArchiveDisplayType, Unknown]]
    archive_published_at: Optional[datetime]
    release_condition_id: Optional[datetime]
    scenario_id: Optional[str]
    action_set_type: Optional[Union[ActionSetType, Unknown]]
    special_season_id: Optional[int]


class Area(Model):
    id: Optional[int]
    asset_bundle_name: Optional[str]
    area_type: Optional[Union[AreaType, Unknown]]
    view_type: Optional[Union[ViewType, Unknown]]
    name: Optional[str]
    release_condition_id: Optional[int]
    label: Optional[str]
    start_at: Optional[datetime]
    end_at: Optional[datetime]


class AreaPlaylist(Model):
    id: Optional[int]
    area_id: Optional[int]
    music_id: Optional[int]
    asset_bundle_name: Optional[str]
    bgm_name: Optional[str]
    release_condition_id: Optional[int]


class MobCharacter(Model):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    gender: Optional[Union[Gender, Unknown]]


class CharacterCostume(Model):
    id: Optional[int]
    character_id: Optional[int]
    costume_id: Optional[int]
    sd_asset_bundle_name: Optional[str]
    live2d_asset_bundle_name: Optional[str]


class CardCostume3d(Model):
    card_id: Optional[int]
    costume3d_id: Optional[int]


class CardParameter(Model):
    id: Optional[int]
    card_id: Optional[int]
    card_level: Optional[int]
    card_parameter_type: Optional[Union[CardParameterType, Unknown]]
    power: Optional[int]


class Cost(Model):
    resource_id: Optional[int]
    resource_type: Optional[Union[ResourceType, Unknown]]
    resource_level: Optional[int]
    quantity: Optional[int]


class SpecialTrainingCost(Model):
    card_id: Optional[int]
    seq: Optional[int]
    cost: Optional[Cost]


class MasterLessonAchieveResource(Model):
    release_condition_id: Optional[int]
    card_id: Optional[int]
    master_rank: Optional[int]
    resources: Optional[List[Union[dict, str, int]]]


class Card(Model):
    id: Optional[int]
    seq: Optional[int]
    character_id: Optional[int]
    card_rarity_type: Optional[Union[CardRarityType, Unknown]]
    special_training_power1_bonus_fixed: Optional[int]
    special_training_power2_bonus_fixed: Optional[int]
    special_training_power3_bonus_fixed: Optional[int]
    attr: Optional[Union[CardAttr, Unknown]]
    supportunit: Optional[Union[Unit, Unknown]]
    skill_id: Optional[int]
    card_skill_name: Optional[str]
    prefix: Optional[str]
    asset_bundle_name: Optional[str]
    gacha_phrase: Optional[str]
    flavor_text: Optional[str]
    release_at: Optional[datetime]
    archive_published_at: Optional[datetime]
    card_parameters: Optional[List[CardParameter]]
    special_training_costs: Optional[List[SpecialTrainingCost]]
    master_lesson_achieve_resources: Optional[List[MasterLessonAchieveResource]]
    archive_display_type: Optional[Union[ArchiveDisplayType, Unknown]]


class SkillEffectDetail(Model):
    id: Optional[int]
    level: Optional[int]
    activate_effect_duration: Optional[float]
    activate_effect_value_type: Optional[Union[ActivateEffectValueType, Unknown]]
    activate_effect_value: Optional[int]


class SkillEnhanceCondition(Model):
    id: Optional[int]
    seq: Optional[int]
    unit: Optional[Union[Unit, Unknown]]


class SkillEnhance(Model):
    id: Optional[int]
    skill_enhance_type: Optional[Union[SkillEnhanceType, Unknown]]
    activate_effect_value_type: Optional[Union[ActivateEffectValueType, Unknown]]
    activate_effect_value: Optional[int]
    skill_enhance_condition: Optional[SkillEnhanceCondition]


class SkillEffect(Model):
    id: Optional[int]
    skill_effect_type: Optional[Union[SkillEffectType, Unknown]]
    activate_notes_judgment_type: Optional[Union[IngameNoteJudgeType, Unknown]]
    skill_effect_details: Optional[List[SkillEffectDetail]]
    activate_life: Optional[int]
    condition_type: Optional[Union[SkillEffectConditionType, Unknown]]
    skill_enhance: Optional[SkillEnhance]


class Skill(Model):
    id: Optional[int]
    short_description: Optional[str]
    description: Optional[str]
    description_sprite_name: Optional[str]
    skill_filter_id: Optional[int]
    skill_effects: Optional[List[SkillEffect]]


class CardEpisode(Model):
    id: Optional[int]
    seq: Optional[int]
    card_id: Optional[int]
    title: Optional[str]
    scenario_id: Optional[str]
    asset_bundle_name: Optional[str]
    release_condition_id: Optional[int]
    power1_bonus_fixed: Optional[int]
    power2_bonus_fixed: Optional[int]
    power3_bonus_fixed: Optional[int]
    reward_resource_box_ids: Optional[List[int]]
    costs: Optional[List[Cost]]
    card_episode_part_type: Optional[Union[CardEpisodePartType, Unknown]]


class CardRarity(Model):
    card_rarity_type: Optional[Union[CardRarityType, Unknown]]
    seq: Optional[int]
    max_level: Optional[int]
    max_skill_level: Optional[int]
    training_max_level: Optional[int]


class CardSkillCost(Model):
    id: Optional[int]
    material_id: Optional[int]
    exp: Optional[int]


class Music(Model):
    id: Optional[int]
    seq: Optional[int]
    release_condition_id: Optional[int]
    categories: Optional[List[Union[MusicCategory, Unknown]]]
    title: Optional[str]
    pronunciation: Optional[str]
    lyricist: Optional[str]
    composer: Optional[str]
    arranger: Optional[str]
    dancer_count: Optional[int]
    self_dancer_position: Optional[int]
    asset_bundle_name: Optional[str]
    live_talk_background_asset_bundle_name: Optional[str]
    published_at: Optional[datetime]
    live_stage_id: Optional[int]
    filler_sec: Optional[float]
    music_collaboration_id: Optional[int]


class MusicTag(Model):
    id: Optional[int]
    music_id: Optional[int]
    music_tag: Optional[str]
    seq: Optional[int]


class MusicDifficulty(Model):
    id: Optional[int]
    music_id: Optional[int]
    music_difficulty: Optional[Union[MusicDifficultyType, Unknown]]
    play_level: Optional[int]
    release_condition_id: Optional[int]
    note_count: Optional[int]


class Character(Model):
    id: Optional[int]
    music_id: Optional[int]
    music_vocal_id: Optional[int]
    character_type: Optional[Union[CharacterType, Unknown]]
    character_id: Optional[int]
    seq: Optional[int]


class MusicVocal(Model):
    id: Optional[int]
    music_id: Optional[int]
    music_vocal_type: Optional[Union[MusicVocalType, Unknown]]
    seq: Optional[int]
    release_condition_id: Optional[int]
    caption: Optional[str]
    characters: Optional[List[Character]]
    asset_bundle_name: Optional[str]
    archive_published_at: Optional[datetime]
    special_season_id: Optional[int]
    archive_display_type: Optional[Union[ArchiveDisplayType, Unknown]]


class MusicDanceMember(Model):
    id: Optional[int]
    music_id: Optional[int]
    default_music_type: Optional[Union[DefaultMusicType, Unknown]]
    character_id1: Optional[int]
    unit1: Optional[Union[Unit, Unknown]]
    character_id2: Optional[int]
    unit2: Optional[Union[Unit, Unknown]]
    character_id3: Optional[int]
    unit3: Optional[Union[Unit, Unknown]]
    character_id4: Optional[int]
    unit4: Optional[Union[Unit, Unknown]]
    character_id5: Optional[int]
    unit5: Optional[Union[Unit, Unknown]]


class MusicAchievement(Model):
    id: Optional[int]
    music_achievement_type: Optional[Union[MusicAchievementType, Unknown]]
    music_achievement_type_value: Optional[str]
    resource_box_id: Optional[int]
    music_difficulty_type: Optional[Union[MusicDifficultyType, Unknown]]


class MusicVideoCharacter(Model):
    id: Optional[int]
    music_id: Optional[int]
    default_music_type: Optional[Union[DefaultMusicType, Unknown]]
    game_character_unit_id: Optional[int]
    dance_priority: Optional[int]
    seq: Optional[int]
    priority: Optional[int]


class MusicAssetVariant(Model):
    id: Optional[int]
    music_vocal_id: Optional[int]
    seq: Optional[int]
    music_asset_type: Optional[Union[MusicAssetType, Unknown]]
    asset_bundle_name: Optional[str]


class MusicCollaboration(Model):
    id: Optional[int]
    label: Optional[str]


class EpisodeMusicVideoCostume(Model):
    id: Optional[int]
    music_vocal_id: Optional[int]
    character3d_id1: Optional[int]
    character3d_id2: Optional[int]
    character3d_id3: Optional[int]
    character3d_id4: Optional[int]
    character3d_id5: Optional[int]


class ReleaseCondition(Model):
    id: Optional[int]
    sentence: Optional[str]
    release_condition_type: Optional[Union[ReleaseConditionType, Unknown]]
    release_condition_type_level: Optional[int]
    release_condition_type_id: Optional[int]
    release_condition_type_quantity: Optional[int]


class PlayLevelScore(Model):
    live_type: Optional[Union[LiveType, Unknown]]
    play_level: Optional[int]
    s: Optional[int]
    a: Optional[int]
    b: Optional[int]
    c: Optional[int]


class IngameCombo(Model):
    id: Optional[int]
    from_count: Optional[int]
    to_count: Optional[int]
    score_coefficient: Optional[float]


class IngameNote(Model):
    id: Optional[int]
    ingame_note_type: Optional[Union[IngameNoteType, Unknown]]
    score_coefficient: Optional[float]
    damage_bad: Optional[int]
    damage_miss: Optional[int]


class IngameNoteJudge(Model):
    id: Optional[int]
    ingame_note_jadge_type: Optional[Union[IngameNoteJudgeType, Unknown]]
    score_coefficient: Optional[float]
    damage: Optional[int]


class IngamePlayLevel(Model):
    play_level: Optional[int]
    score_coefficient: Optional[float]


class IngameCutin(Model):
    id: Optional[int]
    music_difficulty: Optional[Union[MusicDifficultyType, Unknown]]
    combo: Optional[int]


class IngameCutinCharacter(Model):
    id: Optional[int]
    ingame_cutin_character_type: Optional[Union[IngameCutinCharacterType, Unknown]]
    priority: Optional[int]
    game_character_unit_id1: Optional[int]
    game_character_unit_id2: Optional[int]
    asset_bundle_name1: Optional[str]
    asset_bundle_name2: Optional[str]
    release_condition_id: Optional[int]


class IngameJudgeFrame(Model):
    id: Optional[int]
    ingame_note_type: Optional[Union[IngameNoteType, Unknown]]
    perfect: Optional[float]
    great: Optional[float]
    good: Optional[float]
    bad: Optional[float]
    perfect_before: Optional[float]
    perfect_after: Optional[float]
    great_before: Optional[float]
    great_after: Optional[float]
    good_before: Optional[float]
    good_after: Optional[float]
    bad_before: Optional[float]
    bad_after: Optional[float]


class IngameNoteJudgeTechnicalScore(Model):
    id: Optional[int]
    live_type: Optional[Union[LiveType, Unknown]]
    ingame_note_jadge_type: Optional[Union[IngameNoteJudgeType, Unknown]]
    score: Optional[int]


class Shop(Model):
    id: Optional[int]
    seq: Optional[int]
    shop_type: Optional[Union[ShopType, Unknown]]
    area_id: Optional[int]
    name: Optional[str]
    release_condition_id: Optional[int]


class ShopItemCost(Model):
    shop_item_id: Optional[int]
    seq: Optional[int]
    cost: Optional[Cost]


class ShopItem(Model):
    id: Optional[int]
    shop_id: Optional[int]
    seq: Optional[int]
    release_condition_id: Optional[int]
    resource_box_id: Optional[int]
    costs: Optional[List[ShopItemCost]]
    start_at: Optional[datetime]


class Costume3dShopItemCost(Cost):
    id: Optional[int]
    costume3d_shop_item_id: Optional[int]
    seq: Optional[int]


class Costume3dShopItem(Model):
    id: Optional[int]
    seq: Optional[int]
    group_id: Optional[int]
    name: Optional[str]
    body_costume3d_id: Optional[int]
    release_condition_id: Optional[int]
    costs: Optional[List[Costume3dShopItemCost]]
    start_at: Optional[datetime]
    head_costume3d_id: Optional[int]


class AreaItem(Model):
    id: Optional[int]
    area_id: Optional[int]
    name: Optional[str]
    flavor_text: Optional[str]
    spawn_point: Optional[str]
    asset_bundle_name: Optional[str]


class AreaItemLevel(Model):
    area_item_id: Optional[int]
    level: Optional[int]
    targetunit: Optional[Union[Unit, Unknown]]
    target_card_attr: Optional[Union[CardAttr, Unknown]]
    target_game_character_id: Optional[int]
    power1_bonus_rate: Optional[float]
    power1_all_match_bonus_rate: Optional[float]
    power2_bonus_rate: Optional[float]
    power2_all_match_bonus_rate: Optional[float]
    power3_bonus_rate: Optional[float]
    power3_all_match_bonus_rate: Optional[float]
    sentence: Optional[str]


class Material(Model):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    flavor_text: Optional[str]
    material_type: Optional[Union[MaterialType, Unknown]]


class GachaCardRarityRate(Model):
    id: Optional[int]
    group_id: Optional[int]
    card_rarity_type: Optional[Union[CardRarityType, Unknown]]
    lottery_type: Optional[Union[LotteryType, Unknown]]
    rate: Optional[float]


class GachaDetail(Model):
    id: Optional[int]
    gacha_id: Optional[int]
    card_id: Optional[int]
    weight: Optional[int]
    is_wish: Optional[bool]


class GachaBehavior(Model):
    id: Optional[int]
    gacha_id: Optional[int]
    group_id: Optional[int]
    priority: Optional[int]
    gacha_behavior_type: Optional[Union[GachaBehaviorType, Unknown]]
    cost_resource_type: Optional[Union[ResourceType, Unknown]]
    cost_resource_quantity: Optional[int]
    spin_count: Optional[int]
    execute_limit: Optional[int]
    cost_resource_id: Optional[int]
    gacha_extra_id: Optional[int]


class GachaPickup(Model):
    id: Optional[int]
    gacha_id: Optional[int]
    card_id: Optional[int]
    gacha_pickup_type: Optional[Union[GachaPickupType, Unknown]]


class GachaInformation(Model):
    gacha_id: Optional[int]
    summary: Optional[str]
    description: Optional[str]


class Gacha(Model):
    id: Optional[int]
    gacha_type: Optional[Union[GachaType, Unknown]]
    name: Optional[str]
    seq: Optional[int]
    asset_bundle_name: Optional[str]
    gacha_card_rarity_rate_group_id: Optional[int]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    is_show_period: Optional[bool]
    gacha_ceil_item_id: Optional[int]
    wish_select_count: Optional[int]
    wish_fixed_select_count: Optional[int]
    wish_limited_select_count: Optional[int]
    gacha_card_rarity_rates: Optional[List[GachaCardRarityRate]]
    gacha_details: Optional[List[GachaDetail]]
    gacha_behaviors: Optional[List[GachaBehavior]]
    gacha_pickups: Optional[List[GachaPickup]]
    gacha_pickup_costumes: Optional[List[Union[dict, str, int]]]
    gacha_information: Optional[GachaInformation]
    drawable_gacha_hour: Optional[int]
    gacha_bonus_id: Optional[int]
    spin_limit: Optional[int]


class GachaBonus(Model):
    id: Optional[int]


class GachaBonusPoint(Model):
    id: Optional[int]
    resource_type: Optional[Union[ResourceType, Unknown]]
    point: Optional[float]


class GachaExtra(Model):
    id: Optional[int]
    resource_box_id: Optional[int]


class GiftGachaExchange(Model):
    id: Optional[int]
    gacha_id: Optional[int]
    seq: Optional[int]
    resource_box_id: Optional[int]


class PracticeTicket(Model):
    id: Optional[int]
    name: Optional[str]
    exp: Optional[int]
    flavor_text: Optional[str]


class SkillPracticeTicket(PracticeTicket):
    pass


class Level(Model):
    id: Optional[int]
    level_type: Optional[Union[LevelType, Unknown]]
    level: Optional[int]
    total_exp: Optional[int]


class Episode(Model):
    id: Optional[int]
    episode_no: Optional[int]
    title: Optional[str]
    asset_bundle_name: Optional[str]
    scenario_id: Optional[str]
    release_condition_id: Optional[int]
    reward_resource_box_ids: Optional[List[int]]


class UnitStoryEpisode(Episode):
    unit: Optional[Union[Unit, Unknown]]
    chapter_no: Optional[int]
    unit_episode_category: Optional[Union[Unit, Unknown]]
    episode_no_label: Optional[str]
    limited_release_start_at: Optional[datetime]
    limited_release_end_at: Optional[datetime]
    and_release_condition_id: Optional[int]


class Chapter(Model):
    id: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    chapter_no: Optional[int]
    title: Optional[str]
    asset_bundle_name: Optional[str]
    episodes: Optional[List[UnitStoryEpisode]]


class UnitStory(Model):
    unit: Optional[Union[Unit, Unknown]]
    seq: Optional[int]
    asset_bundle_name: Optional[str]
    chapters: Optional[List[Chapter]]


class SpecialStoryEpisode(Episode):
    special_story_id: Optional[int]
    special_story_episode_type: Optional[str]
    is_able_skip: Optional[bool]
    is_action_set_refresh: Optional[bool]
    special_story_episode_type_id: Optional[int]


class SpecialStory(Model):
    id: Optional[int]
    seq: Optional[int]
    title: Optional[str]
    asset_bundle_name: Optional[str]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    episodes: Optional[List[SpecialStoryEpisode]]


class Config(Model):
    config_key: Optional[str]
    value: Optional[str]


class ClientConfig(Model):
    id: Optional[int]
    value: Optional[str]
    type: Optional[Union[ClientConfigType, Unknown]]


class Wording(Model):
    wording_key: Optional[str]
    value: Optional[str]


class Costume3d(Model):
    id: Optional[int]
    seq: Optional[int]
    costume3d_group_id: Optional[int]
    costume3d_type: Optional[Union[Costume3dType, Unknown]]
    name: Optional[str]
    part_type: Optional[Union[PartType, Unknown]]
    color_id: Optional[int]
    color_name: Optional[str]
    character_id: Optional[int]
    costume3d_rarity: Optional[Union[Costume3dRarity, Unknown]]
    how_to_obtain: Optional[str]
    asset_bundle_name: Optional[str]
    designer: Optional[str]
    archive_display_type: Optional[Union[ArchiveDisplayType, Unknown]]
    archive_published_at: Optional[datetime]
    published_at: Optional[datetime]


class Costume3dModel(Model):
    id: Optional[int]
    costume3d_id: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    head_costume3d_asset_bundle_type: Optional[Union[HeadCostume3dAssetBundleType, Unknown]]
    thumbnail_asset_bundle_name: Optional[str]
    asset_bundle_name: Optional[str]
    color_asset_bundle_name: Optional[str]
    part: Optional[str]


class Costume3dModelAvailablePattern(Model):
    id: Optional[int]
    head_costume3d_id: Optional[int]
    hair_costume3d_id: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    is_default: Optional[bool]


class GameCharacterUnit3dMotion(Model):
    id: Optional[int]
    game_character_unit_id: Optional[int]
    motion_type: Optional[Union[MotionType, Unknown]]
    asset_bundle_name: Optional[str]


class Costume2d(Model):
    id: Optional[int]
    costume2d_group_id: Optional[int]
    character2d_id: Optional[int]
    from_mmddhh: Optional[str]
    to_mmddhh: Optional[str]
    live2d_asset_bundle_name: Optional[str]
    spine_asset_bundle_name: Optional[str]


class Costume2dGroup(Model):
    id: Optional[int]
    name: Optional[str]


class Topic(Model):
    id: Optional[int]
    topic_type: Optional[Union[TopicType, Unknown]]
    topic_type_id: Optional[int]
    release_condition_id: Optional[int]


class LiveStage(Model):
    id: Optional[int]
    name: Optional[str]
    asset_bundle_name: Optional[str]


class Stamp(Model):
    id: Optional[int]
    stamp_type: Optional[Union[StampType, Unknown]]
    seq: Optional[int]
    name: Optional[str]
    asset_bundle_name: Optional[str]
    balloon_asset_bundle_name: Optional[str]
    character_id1: Optional[int]
    game_character_unit_id: Optional[int]
    archive_published_at: Optional[datetime]
    description: Optional[str]
    archive_display_type: Optional[Union[ArchiveDisplayType, Unknown]]


class MultiLiveLobby(Model):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    photon_lobby_name: Optional[str]
    matching_logic: Optional[Union[MatchingLogic, Unknown]]
    total_power: Optional[int]
    asset_bundle_name: Optional[str]
    multi_live_lobby_type: Optional[Union[MultiLiveLobbyType, Unknown]]


class MasterLessonCost(Cost):
    id: Optional[int]
    card_rarity_type: Optional[Union[CardRarityType, Unknown]]
    master_rank: Optional[int]
    seq: Optional[int]


class MasterLesson(Model):
    card_rarity_type: Optional[Union[CardRarityType, Unknown]]
    master_rank: Optional[int]
    power1_bonus_fixed: Optional[int]
    power2_bonus_fixed: Optional[int]
    power3_bonus_fixed: Optional[int]
    character_rank_exp: Optional[int]
    costs: Optional[List[MasterLessonCost]]
    rewards: Optional[List[Union[dict, str, int]]]


class MasterLessonReward(Model):
    id: Optional[int]
    card_id: Optional[int]
    master_rank: Optional[int]
    seq: Optional[int]
    resource_box_id: Optional[int]
    card_rarity: Optional[int]


class CardExchangeResource(Model):
    card_rarity_type: Optional[Union[CardRarityType, Unknown]]
    seq: Optional[int]
    resource_box_id: Optional[int]


class MaterialExchangeCost(Cost):
    material_exchange_id: Optional[int]
    cost_group_id: Optional[int]
    seq: Optional[int]


class MaterialExchange(Model):
    id: Optional[int]
    material_exchange_summary_id: Optional[int]
    seq: Optional[int]
    resource_box_id: Optional[int]
    refresh_cycle: Optional[Union[RefreshCycle, Unknown]]
    costs: Optional[List[MaterialExchangeCost]]
    exchange_limit: Optional[int]
    start_at: Optional[datetime]


class MaterialExchangeSummary(Model):
    id: Optional[int]
    seq: Optional[int]
    exchange_category: Optional[Union[ExchangeCategory, Unknown]]
    material_exchange_type: Optional[Union[MaterialExchangeType, Unknown]]
    name: Optional[str]
    asset_bundle_name: Optional[str]
    start_at: Optional[datetime]
    material_exchanges: Optional[List[MaterialExchange]]
    end_at: Optional[datetime]
    notification_remain_hour: Optional[int]


class BoostItem(Model):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    recovery_value: Optional[int]
    asset_bundle_name: Optional[str]
    flavor_text: Optional[str]


class BillingProduct(Model):
    id: Optional[int]
    group_id: Optional[int]
    platform: Optional[Platform]
    product_id: Optional[str]
    price: Optional[int]
    unit_price: Optional[float]


class BillingShopItem(Model):
    id: Optional[int]
    seq: Optional[int]
    billing_shop_item_type: Optional[Union[BillingShopItemType, Unknown]]
    billing_product_group_id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    billable_limit_type: Optional[Union[BillableLimitType, Unknown]]
    billable_limit_reset_interval_type: Optional[Union[BillableLimitResetIntervalType, Unknown]]
    asset_bundle_name: Optional[str]
    resource_box_id: Optional[int]
    billable_limit_value: Optional[int]
    bonus_resource_box_id: Optional[int]
    label: Optional[str]
    end_at: Optional[datetime]
    start_at: Optional[datetime]
    billable_limit_reset_interval_value: Optional[int]
    purchase_option: Optional[Union[PurchaseOption, Unknown]]


class BillingShopItemExchangeCost(Cost):
    id: Optional[int]
    billing_shop_item_id: Optional[int]


class ColorfulPass(Model):
    id: Optional[int]
    resource_box_id: Optional[int]
    receivable_days: Optional[int]
    present_sentence: Optional[str]
    expire_days: Optional[int]
    daily_paid_gacha_spin_limit: Optional[int]
    challenge_live_point_multiple: Optional[int]
    live_point_multiple: Optional[int]


class JewelBehavior(Model):
    id: Optional[int]
    seq: Optional[int]
    jewel_behavior_type: Optional[Union[JewelBehaviorType, Unknown]]
    jewel_behavior_type_quantity: Optional[int]
    amount: Optional[int]


class CharacterRankAchieveResource(Model):
    release_condition_id: Optional[int]
    character_id: Optional[int]
    character_rank: Optional[int]
    resources: Optional[List[Union[dict, str, int]]]


class CharacterRank(Model):
    id: Optional[int]
    character_id: Optional[int]
    character_rank: Optional[int]
    power1_bonus_rate: Optional[float]
    power2_bonus_rate: Optional[float]
    power3_bonus_rate: Optional[float]
    reward_resource_box_ids: Optional[List[int]]
    character_rank_achieve_resources: Optional[List[CharacterRankAchieveResource]]


class CharacterMissionV2(Model):
    id: Optional[int]
    character_mission_type: Optional[Union[CharacterMissionType, Unknown]]
    character_id: Optional[int]
    parameter_group_id: Optional[int]
    sentence: Optional[str]
    progress_sentence: Optional[str]
    is_achievement_mission: Optional[bool]


class CharacterMissionV2ParameterGroup(Model):
    id: Optional[int]
    seq: Optional[int]
    requirement: Optional[int]
    exp: Optional[int]


class CharacterMissionV2AreaItem(Model):
    id: Optional[int]
    character_mission_type: Optional[Union[CharacterMissionType, Unknown]]
    area_item_id: Optional[int]
    character_id: Optional[int]
    unit: Optional[Union[Unit, Unknown]]


class SystemLive2d(Live2d):
    serif: Optional[str]
    voice: Optional[str]
    published_at: Optional[datetime]
    closed_at: Optional[datetime]
    special_season_id: Optional[int]


class Reward(Model):
    id: Optional[int]
    mission_type: Optional[Union[MissionType, Unknown]]
    mission_id: Optional[int]
    seq: Optional[int]
    resource_box_id: Optional[int]


class NormalMission(Model):
    id: Optional[int]
    seq: Optional[int]
    normal_mission_type: Optional[Union[NormalMissionType, Unknown]]
    requirement: Optional[int]
    sentence: Optional[str]
    rewards: Optional[List[Reward]]


class BeginnerMission(Model):
    id: Optional[int]
    seq: Optional[int]
    beginner_mission_type: Optional[Union[BeginnerMissionType, Unknown]]
    beginner_mission_category: Optional[Union[BeginnerMissionCategory, Unknown]]
    requirement: Optional[int]
    sentence: Optional[str]
    rewards: Optional[List[Reward]]


class Detail(Model):
    resource_box_purpose: Optional[Union[ResourceBoxPurpose, Unknown]]
    resource_box_id: Optional[int]
    seq: Optional[int]
    resource_type: Optional[Union[ResourceType, Unknown]]
    resource_quantity: Optional[int]
    resource_id: Optional[int]
    resource_level: Optional[int]


class ResourceBox(Model):
    resource_box_purpose: Optional[Union[ResourceBoxPurpose, Unknown]]
    id: Optional[int]
    resource_box_type: Optional[Union[ResourceBoxType, Unknown]]
    details: Optional[List[Detail]]
    description: Optional[str]
    name: Optional[str]
    asset_bundle_name: Optional[str]


class LiveMissionPeriod(Model):
    id: Optional[int]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    sentence: Optional[str]


class LiveMission(Model):
    id: Optional[int]
    live_mission_period_id: Optional[int]
    live_mission_type: Optional[Union[LiveMissionType, Unknown]]
    requirement: Optional[int]
    rewards: Optional[List[Reward]]


class LiveMissionPass(Model):
    id: Optional[int]
    live_mission_period_id: Optional[int]
    costume_name: Optional[str]
    character3d_id1: Optional[int]
    character3d_id2: Optional[int]
    male_asset_bundle_name: Optional[str]
    female_asset_bundle_name: Optional[str]


class PenlightColor(Model):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    description: Optional[str]
    color_code: Optional[str]
    character_id: Optional[int]
    unit: Optional[Union[Unit, Unknown]]


class Penlight(Model):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    default_penlight_color_id: Optional[int]
    asset_bundle_name: Optional[str]


class LiveTalk(Model):
    id: Optional[int]
    live_talk_type: Optional[Union[LiveTalkType, Unknown]]
    scenario_id: Optional[str]
    character_id1: Optional[int]
    character_id2: Optional[int]


class Tip(Model):
    id: Optional[int]
    title: Optional[str]
    description: Optional[str]
    from_user_rank: Optional[int]
    to_user_rank: Optional[int]
    asset_bundle_name: Optional[str]


class GachaCeilItem(Model):
    id: Optional[int]
    gacha_id: Optional[int]
    name: Optional[str]
    asset_bundle_name: Optional[str]
    convert_start_at: Optional[datetime]
    convert_resource_box_id: Optional[int]


class GachaCeilExchangeCost(Cost):
    gacha_ceil_exchange_id: Optional[int]
    gacha_ceil_item_id: Optional[int]


class GachaCeilExchangeSubstituteCost(Cost):
    id: Optional[int]
    substitute_quantity: Optional[int]


class GachaCeilExchange(Model):
    id: Optional[int]
    gacha_ceil_exchange_summary_id: Optional[int]
    seq: Optional[int]
    resource_box_id: Optional[int]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    gacha_ceil_exchange_cost: Optional[GachaCeilExchangeCost]
    gacha_ceil_exchange_substitute_costs: Optional[List[GachaCeilExchangeSubstituteCost]]
    exchange_limit: Optional[int]
    gacha_ceil_exchange_label_type: Optional[Union[GachaCeilExchangeLabelType, Unknown]]
    substitute_limit: Optional[int]


class GachaCeilExchangeSummary(Model):
    id: Optional[int]
    seq: Optional[int]
    gacha_id: Optional[int]
    asset_bundle_name: Optional[str]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    gacha_ceil_exchanges: Optional[List[GachaCeilExchange]]
    gacha_ceil_item_id: Optional[int]


class PlayerRankReward(Model):
    id: Optional[int]
    player_rank: Optional[int]
    seq: Optional[int]
    resource_box_id: Optional[int]


class GachaTicket(Model):
    id: Optional[int]
    name: Optional[str]
    asset_bundle_name: Optional[str]


class HonorGroup(Model):
    id: Optional[int]
    name: Optional[str]
    honor_type: Optional[Union[HonorType, Unknown]]
    archive_published_at: Optional[datetime]
    background_asset_bundle_name: Optional[str]


class HonorLevel(Model):
    honor_id: Optional[int]
    level: Optional[int]
    bonus: Optional[int]
    description: Optional[str]


class Honor(Model):
    id: Optional[int]
    seq: Optional[int]
    group_id: Optional[int]
    honor_rarity: Optional[Union[HonorRarity, Unknown]]
    name: Optional[str]
    asset_bundle_name: Optional[str]
    levels: Optional[List[HonorLevel]]
    honor_type_id: Optional[int]


class HonorMission(Model):
    id: Optional[int]
    seq: Optional[int]
    honor_mission_type: Optional[Union[HonorMissionType, Unknown]]
    requirement: Optional[int]
    sentence: Optional[str]
    rewards: Optional[List[Reward]]


class BondsHonorLevel(Model):
    id: Optional[int]
    bonds_honor_id: Optional[int]
    level: Optional[int]
    description: Optional[str]


class BondsHonor(Model):
    id: Optional[int]
    seq: Optional[int]
    bonds_group_id: Optional[int]
    game_character_unit_id1: Optional[int]
    game_character_unit_id2: Optional[int]
    honor_rarity: Optional[Union[HonorRarity, Unknown]]
    name: Optional[str]
    description: Optional[str]
    levels: Optional[List[BondsHonorLevel]]
    configurable_unit_virtual_singer: Optional[bool]


class BondsHonorWord(Model):
    id: Optional[int]
    seq: Optional[int]
    bonds_group_id: Optional[int]
    asset_bundle_name: Optional[str]
    name: Optional[str]
    description: Optional[str]


class BondsReward(Model):
    id: Optional[int]
    bonds_group_id: Optional[int]
    rank: Optional[int]
    seq: Optional[int]
    bonds_reward_type: Optional[Union[BondsRewardType, Unknown]]
    resource_box_id: Optional[int]
    description: Optional[str]


class ChallengeLiveDetail(Model):
    id: Optional[int]
    challenge_live_id: Optional[int]
    challenge_live_type: Optional[Union[LiveType, Unknown]]


class ChallengeLive(Model):
    id: Optional[int]
    playable_count: Optional[int]
    challenge_live_details: Optional[List[ChallengeLiveDetail]]


class ChallengeLiveDeck(Model):
    id: Optional[int]
    character_id: Optional[int]
    release_condition_id: Optional[int]
    card_limit: Optional[int]


class ChallengeLiveStage(Model):
    id: Optional[int]
    character_id: Optional[int]
    rank: Optional[int]
    name: Optional[str]
    next_stage_challenge_point: Optional[int]
    complete_stage_resource_box_id: Optional[int]
    complete_stage_character_exp: Optional[int]


class ChallengeLiveStageEx(Model):
    id: Optional[int]
    character_id: Optional[int]
    from_rank: Optional[int]
    to_rank: Optional[int]
    name: Optional[str]
    next_stage_challenge_point: Optional[int]
    complete_stage_resource_box_id: Optional[int]
    complete_stage_character_exp: Optional[int]


class ChallengeLiveHighScoreReward(Model):
    id: Optional[int]
    character_id: Optional[int]
    high_score: Optional[int]
    resource_box_id: Optional[int]


class ChallengeLiveCharacter(Model):
    id: Optional[int]
    character_id: Optional[int]
    release_condition_id: Optional[int]
    or_release_condition_id: Optional[int]


class ChallengeLivePlayDayReward(Model):
    id: Optional[int]
    challenge_live_play_day_reward_period_id: Optional[int]
    play_days: Optional[int]
    seq: Optional[int]
    resource_box_id: Optional[int]


class ChallengeLivePlayDayRewardPeriod(Model):
    id: Optional[int]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    priority: Optional[int]
    challenge_live_play_day_rewards: Optional[List[ChallengeLivePlayDayReward]]


class VirtualLiveSetlist(Model):
    id: Optional[int]
    virtual_live_id: Optional[int]
    seq: Optional[int]
    virtual_live_setlist_type: Optional[Union[VirtualLiveSetlistType, Unknown]]
    asset_bundle_name: Optional[str]
    virtual_live_stage_id: Optional[int]
    music_id: Optional[int]
    music_vocal_id: Optional[int]
    character3d_id1: Optional[int]
    character3d_id2: Optional[int]
    character3d_id3: Optional[int]
    character3d_id4: Optional[int]
    character3d_id5: Optional[int]
    character3d_id6: Optional[int]


class VirtualLiveBeginnerSchedule(Model):
    id: Optional[int]
    virtual_live_id: Optional[int]
    day_of_week: Optional[Union[DayOfWeek, Unknown]]
    start_time: Optional[str]
    end_time: Optional[str]


class VirtualLiveSchedule(Model):
    id: Optional[int]
    virtual_live_id: Optional[int]
    seq: Optional[int]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    notice_group_id: Optional[str]


class VirtualLiveCharacter(Model):
    id: Optional[int]
    virtual_live_id: Optional[int]
    game_character_unit_id: Optional[int]
    seq: Optional[int]


class VirtualLiveReward(Model):
    id: Optional[int]
    virtual_live_type: Optional[Union[VirtualLiveType, Unknown]]
    virtual_live_id: Optional[int]
    resource_box_id: Optional[int]


class VirtualLiveWaitingRoom(Model):
    id: Optional[int]
    virtual_live_id: Optional[int]
    asset_bundle_name: Optional[str]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    lobby_asset_bundle_name: Optional[str]


class VirtualItem(Model):
    id: Optional[int]
    virtual_item_category: Optional[Union[VirtualItemCategory, Unknown]]
    seq: Optional[int]
    priority: Optional[int]
    name: Optional[str]
    asset_bundle_name: Optional[str]
    cost_virtual_coin: Optional[int]
    cost_jewel: Optional[int]
    cheer_point: Optional[int]
    effect_asset_bundle_name: Optional[str]
    effect_expression_type: Optional[Union[EffectExpressionType, Unknown]]
    unit: Optional[Union[Unit, Unknown]]
    game_character_unit_id: Optional[int]
    virtual_item_label_type: Optional[Union[VirtualItemLabelType, Unknown]]


class VirtualLiveAppeal(Model):
    id: Optional[int]
    virtual_live_id: Optional[int]
    virtual_live_stage_status: Optional[Union[VirtualLiveStageStatus, Unknown]]
    appeal_text: Optional[str]


class VirtualLiveInformation(Model):
    virtual_live_id: Optional[int]
    summary: Optional[str]
    description: Optional[str]


class VirtualLive(Model):
    id: Optional[int]
    virtual_live_type: Optional[Union[VirtualLiveType, Unknown]]
    virtual_live_platform: Optional[str]
    seq: Optional[int]
    name: Optional[str]
    asset_bundle_name: Optional[str]
    screen_mv_music_vocal_id: Optional[int]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    ranking_announce_at: Optional[datetime]
    virtual_live_setlists: Optional[List[VirtualLiveSetlist]]
    virtual_live_beginner_schedules: Optional[List[VirtualLiveBeginnerSchedule]]
    virtual_live_schedules: Optional[List[VirtualLiveSchedule]]
    virtual_live_characters: Optional[List[VirtualLiveCharacter]]
    virtual_live_reward: Optional[VirtualLiveReward]
    virtual_live_rewards: Optional[List[VirtualLiveReward]]
    virtual_live_cheer_point_rewards: Optional[List[Union[dict, str, int]]]
    virtual_live_waiting_room: Optional[VirtualLiveWaitingRoom]
    virtual_items: Optional[List[VirtualItem]]
    virtual_live_appeals: Optional[List[VirtualLiveAppeal]]
    virtual_live_information: Optional[VirtualLiveInformation]
    archive_release_condition_id: Optional[int]
    virtual_live_ticket_id: Optional[int]


class VirtualShopItem(Model):
    id: Optional[int]
    virtual_shop_id: Optional[int]
    virtual_shop_item_type: Optional[Union[VirtualShopItemType, Unknown]]
    seq: Optional[int]
    resource_box_id: Optional[int]
    cost_virtual_coin: Optional[int]
    cost_jewel: Optional[int]
    start_at: Optional[datetime]
    cost_paid_jewel: Optional[int]
    end_at: Optional[datetime]
    limit_value: Optional[int]


class VirtualShop(Model):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    virtual_shop_items: Optional[List[VirtualShopItem]]
    virtual_shop_type: Optional[Union[VirtualShopType, Unknown]]
    virtual_live_id: Optional[int]


class VirtualLiveCheerMessage(Model):
    id: Optional[int]
    virtual_live_type: Optional[Union[VirtualLiveType, Unknown]]
    resource_type: Optional[Union[ResourceType, Unknown]]
    from_cost_virtual_coin: Optional[int]
    to_cost_virtual_coin: Optional[int]
    from_cost: Optional[int]
    to_cost: Optional[int]
    asset_bundle_name: Optional[str]
    message_length_limit: Optional[int]
    display_sec: Optional[float]
    message_size: Optional[str]
    color_code: Optional[str]
    virtual_live_cheer_message_display_limit_id: Optional[int]


class VirtualLiveCheerMessageDisplayLimit(Model):
    id: Optional[int]
    display_limit: Optional[int]


class VirtualLiveTicket(Model):
    id: Optional[int]
    virtual_live_id: Optional[int]
    virtual_live_ticket_type: Optional[Union[VirtualLiveTicketType, Unknown]]
    name: Optional[str]
    flavor_text: Optional[str]
    asset_bundle_name: Optional[str]


class VirtualLivePamphlet(Model):
    id: Optional[int]
    virtual_live_id: Optional[int]
    name: Optional[str]
    flavor_text: Optional[str]
    asset_bundle_name: Optional[str]


class AvatarAccessory(Model):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    part: Optional[Union[AccessoryPart, Unknown]]
    asset_bundle_name: Optional[str]


class AvatarCostume(Model):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    asset_bundle_name: Optional[str]


class AvatarMotion(Model):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    sync_music_flg: Optional[bool]
    repeat_count: Optional[int]
    asset_bundle_name: Optional[str]


class AvatarSkinColor(Model):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    color_code: Optional[str]


class AvatarCoordinate(Model):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    asset_bundle_name: Optional[str]
    skin_color_code: Optional[str]
    costume_asset_bundle_name: Optional[str]
    accessory_part: Optional[Union[AccessoryPart, Unknown]]
    accessory_asset_bundle_name: Optional[str]


class NgWord(Model):
    id: Optional[int]
    word: Optional[str]


class RuleSlide(Model):
    id: Optional[int]
    rule_slide_type: Optional[Union[RuleSlideType, Unknown]]
    asset_bundle_name: Optional[str]


class Facility(Model):
    id: Optional[int]
    facility_type: Optional[Union[FacilityType, Unknown]]
    release_condition_id: Optional[int]
    and_release_condition_id: Optional[int]


class OneTimeBehavior(Model):
    id: Optional[int]
    one_time_behavior_type: Optional[Union[OneTimeBehaviorType, Unknown]]
    release_condition_id: Optional[int]


class LoginBonus(Model):
    id: Optional[int]
    day: Optional[int]
    resource_box_id: Optional[int]


class BeginnerLoginBonus(Model):
    id: Optional[int]
    day: Optional[int]
    resource_box_id: Optional[int]
    login_bonus_id: Optional[int]


class BeginnerLoginBonusSummary(Model):
    id: Optional[int]
    login_bonus_id: Optional[int]
    start_at: Optional[datetime]
    end_at: Optional[datetime]


class LimitedLoginBonusDetail(Model):
    id: Optional[int]
    limited_login_bonus_id: Optional[int]
    day: Optional[int]
    resource_box_id: Optional[int]


class LimitedLoginBonus(Model):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    asset_bundle_name: Optional[str]
    close_at: Optional[datetime]
    limited_login_bonus_details: Optional[List[LimitedLoginBonusDetail]]


class LoginBonusLive2d(Live2d):
    serif: Optional[str]
    voice: Optional[str]
    published_at: Optional[datetime]
    closed_at: Optional[datetime]


class EventRankingReward(Model):
    id: Optional[int]
    event_ranking_reward_range_id: Optional[int]
    resource_box_id: Optional[int]


class EventRankingRewardRange(Model):
    id: Optional[int]
    event_id: Optional[int]
    from_rank: Optional[int]
    to_rank: Optional[int]
    event_ranking_rewards: Optional[List[EventRankingReward]]


class Event(Model):
    id: Optional[int]
    event_type: Optional[Union[EventType, Unknown]]
    name: Optional[str]
    asset_bundle_name: Optional[str]
    bgm_asset_bundle_name: Optional[str]
    start_at: Optional[datetime]
    aggregate_at: Optional[datetime]
    ranking_announce_at: Optional[datetime]
    distribution_start_at: Optional[datetime]
    closed_at: Optional[datetime]
    distribution_end_at: Optional[datetime]
    virtual_live_id: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    event_ranking_reward_ranges: Optional[List[EventRankingRewardRange]]
    event_point_asset_bundle_name: Optional[str]


class EventMusic(Model):
    event_id: Optional[int]
    music_id: Optional[int]
    seq: Optional[int]
    release_condition_id: Optional[int]


class EventDeckBonus(Model):
    id: Optional[int]
    event_id: Optional[int]
    game_character_unit_id: Optional[int]
    card_attr: Optional[Union[CardAttr, Unknown]]
    bonus_rate: Optional[float]


class EventRarityBonusRate(Model):
    id: Optional[int]
    card_rarity_type: Optional[Union[CardRarityType, Unknown]]
    master_rank: Optional[int]
    bonus_rate: Optional[float]


class EventItem(Model):
    id: Optional[int]
    event_id: Optional[int]
    name: Optional[str]
    flavor_text: Optional[str]
    asset_bundle_name: Optional[str]


class EpisodeReward(Model):
    story_type: Optional[Union[StoryType, Unknown]]
    resource_box_id: Optional[int]


class EventStoryEpisode(Model):
    id: Optional[int]
    event_story_id: Optional[int]
    episode_no: Optional[int]
    title: Optional[str]
    asset_bundle_name: Optional[str]
    scenario_id: Optional[str]
    release_condition_id: Optional[int]
    episode_rewards: Optional[List[EpisodeReward]]


class EventStory(Model):
    id: Optional[int]
    event_id: Optional[int]
    asset_bundle_name: Optional[str]
    event_story_episodes: Optional[List[EventStoryEpisode]]


class EventExchangeCost(Cost):
    id: Optional[int]
    event_exchange_id: Optional[int]


class EventExchange(Model):
    id: Optional[int]
    event_exchange_summary_id: Optional[int]
    seq: Optional[int]
    resource_box_id: Optional[int]
    exchange_limit: Optional[int]
    event_exchange_cost: Optional[EventExchangeCost]


class EventExchangeSummary(Model):
    id: Optional[int]
    event_id: Optional[int]
    asset_bundle_name: Optional[str]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    event_exchanges: Optional[List[EventExchange]]


class EventStoryUnit(Model):
    id: Optional[int]
    seq: Optional[int]
    event_story_id: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    event_story_unit_relation: Optional[Union[EventStoryUnitRelation, Unknown]]


class EventCard(Model):
    id: Optional[int]
    card_id: Optional[int]
    event_id: Optional[int]
    bonus_rate: Optional[float]


class PreliminaryTournamentCard(Model):
    id: Optional[int]
    preliminary_tournament_id: Optional[int]
    card_id: Optional[int]


class PreliminaryTournamentMusic(Model):
    id: Optional[int]
    preliminary_tournament_id: Optional[int]
    music_difficulty_id: Optional[int]
    music_id: Optional[int]


class PreliminaryTournament(Model):
    id: Optional[int]
    preliminary_tournament_type: Optional[Union[PreliminaryTournamentType, Unknown]]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    release_condition_id: Optional[int]
    preliminary_tournament_cards: Optional[List[PreliminaryTournamentCard]]
    preliminary_tournament_musics: Optional[List[PreliminaryTournamentMusic]]


class CheerfulCarnivalSummary(Model):
    id: Optional[int]
    event_id: Optional[int]
    theme: Optional[str]
    midterm_announce1_at: Optional[datetime]
    midterm_announce2_at: Optional[datetime]
    asset_bundle_name: Optional[str]


class CheerfulCarnivalTeam(Model):
    id: Optional[int]
    event_id: Optional[int]
    seq: Optional[int]
    team_name: Optional[str]
    asset_bundle_name: Optional[str]


class CheerfulCarnivalPartyName(Model):
    id: Optional[int]
    party_name: Optional[str]
    game_character_unit_id1: Optional[int]
    game_character_unit_id2: Optional[int]
    game_character_unit_id3: Optional[int]
    game_character_unit_id4: Optional[int]
    game_character_unit_id5: Optional[int]


class CheerfulCarnivalCharacterPartyName(Model):
    id: Optional[int]
    character_party_name: Optional[str]
    game_character_unit_id: Optional[int]


class CheerfulCarnivalLiveTeamPointBonus(Model):
    id: Optional[int]
    team_point_bonus_rate: Optional[int]


class CheerfulCarnivalReward(Model):
    id: Optional[int]
    event_id: Optional[int]
    cheerful_carnival_team_id: Optional[int]
    resource_box_id: Optional[int]


class CheerfulCarnivalResultReward(Model):
    id: Optional[int]
    event_id: Optional[int]
    cheerful_carnival_team_point_term_type: Optional[Union[CheerfulCarnivalTeamPointTermType, Unknown]]
    cheerful_carnival_result_type: Optional[Union[CheerfulCarnivalResultType, Unknown]]
    resource_box_id: Optional[int]


class Appeal(Model):
    id: Optional[int]
    seq: Optional[int]
    appeal_target_type: Optional[Union[AppealTargetType, Unknown]]
    appeal_type: Optional[Union[AppealType, Unknown]]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    appeal_read_condition_type: Optional[Union[AppealReadConditionType, Unknown]]
    text: Optional[str]


class Boost(Model):
    id: Optional[int]
    cost_boost: Optional[int]
    is_event_only: Optional[bool]
    exp_rate: Optional[int]
    reward_rate: Optional[int]
    live_point_rate: Optional[int]
    event_point_rate: Optional[int]
    bonds_exp_rate: Optional[int]


class BoostPresent(Model):
    id: Optional[int]
    seq: Optional[int]
    recovery_value: Optional[int]
    present_limit: Optional[int]
    asset_bundle_name: Optional[str]
    is_unlimited_receive: Optional[bool]
    boost_present_cost_id: Optional[int]


class BoostPresentCost(Cost):
    id: Optional[int]


class EpisodeCharacter(Model):
    id: Optional[int]
    seq: Optional[int]
    character2d_id: Optional[int]
    story_type: Optional[Union[StoryType, Unknown]]
    episode_id: Optional[int]


class CustomProfileTextColor(Model):
    id: Optional[int]
    seq: Optional[int]
    color_code: Optional[str]


class CustomProfileTextFont(Model):
    id: Optional[int]
    name: Optional[str]
    font_name: Optional[str]
    asset_bundle_name: Optional[str]


class CustomProfileResource(Model):
    custom_profile_resource_type: Optional[Union[CustomProfileResourceType, Unknown]]
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    resource_load_type: Optional[Union[ResourceLoadType, Unknown]]
    resource_load_val: Optional[str]
    file_name: Optional[str]


class CustomProfilePlayerInfoResource(CustomProfileResource):
    pass


class CustomProfileGeneralBackgroundResource(CustomProfileResource):
    pass


class CustomProfileStoryBackgroundResource(CustomProfileResource):
    pass


class CustomProfileCollectionResource(CustomProfileResource):
    custom_profile_resource_collection_type: Optional[Union[CustomProfileResourceCollectionType, Unknown]]
    group_id: Optional[int]


class CustomProfileMemberStandingPictureResource(CustomProfileResource):
    character_id: Optional[int]


class CustomProfileShapeResource(CustomProfileResource):
    pass


class CustomProfileEtcResource(CustomProfileResource):
    pass


class CustomProfileGachaBehavior(Model):
    id: Optional[int]
    custom_profile_gacha_id: Optional[int]
    seq: Optional[int]
    cost_resource_type: Optional[Union[ResourceType, Unknown]]
    cost_resource_quantity: Optional[int]
    spin_count: Optional[int]


class CustomProfileGachaDetail(Model):
    id: Optional[int]
    custom_profile_gacha_id: Optional[int]
    custom_profile_resource_type: Optional[Union[CustomProfileResourceType, Unknown]]
    custom_profile_resource_id: Optional[int]
    custom_profile_resource_quantity: Optional[int]
    weight: Optional[int]


class CustomProfileGacha(Model):
    id: Optional[int]
    name: Optional[str]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    asset_bundle_name: Optional[str]
    description: Optional[str]
    notice: Optional[str]
    custom_profile_gacha_behaviors: Optional[List[CustomProfileGachaBehavior]]
    custom_profile_gacha_details: Optional[List[CustomProfileGachaDetail]]


class StreamingLiveBgm(Model):
    id: Optional[int]
    virtual_live_id: Optional[int]
    seq: Optional[int]
    music_vocal_id: Optional[int]


class Omikuji(Model):
    id: Optional[int]
    omikuji_group_id: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    fortune_type: Optional[Union[FortuneType, Unknown]]
    summary: Optional[str]
    title1: Optional[str]
    description1: Optional[str]
    title2: Optional[str]
    description2: Optional[str]
    title3: Optional[str]
    description3: Optional[str]
    unit_asset_bundle_name: Optional[str]
    fortune_asset_bundle_name: Optional[str]
    omikuji_cover_asset_bundle_name: Optional[str]
    unit_file_path: Optional[str]
    fortune_file_path: Optional[str]
    omikuji_cover_file_path: Optional[str]


class OmikujiGroup(Model):
    id: Optional[int]
    name: Optional[str]
    summary: Optional[str]
    description: Optional[str]
    asset_bundle_name: Optional[str]
    appeal_asset_bundle_name: Optional[str]
    sound_asset_bundle_name: Optional[str]


class OmikujiRate(Model):
    id: Optional[int]
    omikuji_group_id: Optional[int]
    fortune_type: Optional[Union[FortuneType, Unknown]]
    rate: Optional[float]


class OmikujiCost(Cost):
    id: Optional[int]
    omikuji_group_id: Optional[int]
    seq: Optional[int]


class OmikujiReward(Model):
    id: Optional[int]
    omikuji_group_id: Optional[int]
    seq: Optional[int]
    resource_type: Optional[Union[ResourceType, Unknown]]
    resource_id: Optional[int]
    resource_quantity: Optional[int]


class VirtualBoothShop(Model):
    id: Optional[int]
    virtual_live_id: Optional[int]
    virtual_booth_shop_type: Optional[Union[VirtualBoothShopType, Unknown]]
    target_id: Optional[int]


class SpecialSeason(Model):
    id: Optional[int]
    special_season_type: Optional[Union[SpecialSeasonType, Unknown]]
    start_at: Optional[datetime]
    end_at: Optional[datetime]
    priority: Optional[int]


class SpecialSeasonArea(Model):
    id: Optional[int]
    special_season_id: Optional[int]
    area_id: Optional[int]
    asset_bundle_name: Optional[str]
    file_name: Optional[str]
    special_season_area_use_type: Optional[Union[SpecialSeasonAreaUseType, Unknown]]


class RankMatchPenalty(Model):
    id: Optional[int]
    count: Optional[int]
    rank_match_penalty_type: Optional[Union[RankMatchPenaltyType, Unknown]]
    rank_match_penalty_type_value: Optional[int]


class RankMatchPlacement(Model):
    id: Optional[int]
    rank_match_placement_condition_type: Optional[str]
    tier_behavior_type: Optional[Union[TierBehaviorType, Unknown]]
    tier_behavior_type_value: Optional[int]
    rank_match_placement_condition_type_value: Optional[int]


class RankMatchBonusPointCondition(Model):
    id: Optional[int]
    rank_match_bonus_point_condition_type: Optional[Union[RankMatchBonusPointConditionType, Unknown]]
    group_id: Optional[int]
    priority: Optional[int]
    calc_type: Optional[Union[CalcType, Unknown]]
    bonus_point: Optional[int]


class RankMatchSeasonPlayableTime(Model):
    id: Optional[int]
    rank_match_season_id: Optional[int]
    start_time: Optional[str]
    end_time: Optional[str]


class RankMatchSeasonTierMusicPlayLevel(Model):
    id: Optional[int]
    rank_match_season_id: Optional[int]
    rank_match_tier_id: Optional[int]
    from_play_level: Optional[int]
    to_play_level: Optional[int]


class RankMatchSeasonTierReward(Model):
    id: Optional[int]
    rank_match_season_id: Optional[int]
    rank_match_tier_id: Optional[int]
    resource_box_id: Optional[int]


class RankMatchSeason(Model):
    id: Optional[int]
    name: Optional[str]
    start_at: Optional[datetime]
    aggregated_at: Optional[datetime]
    ranking_published_at: Optional[datetime]
    batch_execution_at: Optional[datetime]
    distribution_start_at: Optional[datetime]
    distribution_end_at: Optional[datetime]
    closed_at: Optional[datetime]
    asset_bundle_name: Optional[str]
    is_display_result: Optional[bool]
    rank_match_season_playable_times: Optional[List[RankMatchSeasonPlayableTime]]
    rank_match_season_tier_music_play_levels: Optional[
        List[RankMatchSeasonTierMusicPlayLevel]
    ]
    rank_match_season_tier_rewards: Optional[List[RankMatchSeasonTierReward]]


class RankMatchTier(Model):
    id: Optional[int]
    rank_match_grade_id: Optional[int]
    rank_match_class_id: Optional[int]
    tier: Optional[int]
    total_music_difficulty: Optional[int]
    point: Optional[int]
    grade_asset_bundle_name: Optional[str]
    tier_asset_bundle_name: Optional[str]


class RankMatchTierBonusPoint(Model):
    id: Optional[int]
    rank_match_tier_id: Optional[int]
    max_bonus_point: Optional[int]
    reward_point: Optional[int]


class RankMatchGrade(Costume2dGroup):
    id: Optional[int]
    name: Optional[str]


class RankMatchClass(Costume2dGroup):
    id: Optional[int]
    name: Optional[str]


class LimitedTitleScreen(Model):
    id: Optional[int]
    priority: Optional[int]
    download_start_at: Optional[datetime]
    download_end_at: Optional[datetime]
    display_start_at: Optional[datetime]
    display_end_at: Optional[datetime]
    bg_asset_bundle_name: Optional[str]
    logo_asset_bundle_name: Optional[str]
    bgm_asset_bundle_name: Optional[str]
    start_effect_asset_bundle_name: Optional[str]


class MasterData(Model):
    game_characters: Optional[List[GameCharacter]]
    game_character_units: Optional[List[GameCharacterUnit]]
    outside_characters: Optional[List[OutsideCharacter]]
    character3ds: Optional[List[Character3d]]
    character2ds: Optional[List[Character2d]]
    character_profiles: Optional[List[CharacterProfile]]
    bonds: Optional[List[Bond]]
    bonds_live2ds: Optional[List[BondsLive2d]]
    bonds_rank_up_live2ds: Optional[List[BondsRankUpLive2d]]
    unit_profiles: Optional[List[UnitProfile]]
    action_sets: Optional[List[ActionSet]]
    areas: Optional[List[Area]]
    area_playlists: Optional[List[AreaPlaylist]]
    mob_characters: Optional[List[MobCharacter]]
    character_costumes: Optional[List[CharacterCostume]]
    card_costume3ds: Optional[List[CardCostume3d]]
    cards: Optional[List[Card]]
    skills: Optional[List[Skill]]
    card_episodes: Optional[List[CardEpisode]]
    card_rarities: Optional[List[CardRarity]]
    card_skill_costs: Optional[List[CardSkillCost]]
    musics: Optional[List[Music]]
    music_tags: Optional[List[MusicTag]]
    music_difficulties: Optional[List[MusicDifficulty]]
    music_vocals: Optional[List[MusicVocal]]
    music_dance_members: Optional[List[MusicDanceMember]]
    music_achievements: Optional[List[MusicAchievement]]
    music_video_characters: Optional[List[MusicVideoCharacter]]
    music_asset_variants: Optional[List[MusicAssetVariant]]
    music_collaborations: Optional[List[MusicCollaboration]]
    episode_music_video_costumes: Optional[List[EpisodeMusicVideoCostume]]
    release_conditions: Optional[List[ReleaseCondition]]
    play_level_scores: Optional[List[PlayLevelScore]]
    ingame_combos: Optional[List[IngameCombo]]
    ingame_notes: Optional[List[IngameNote]]
    ingame_note_judges: Optional[List[IngameNoteJudge]]
    ingame_play_levels: Optional[List[IngamePlayLevel]]
    ingame_cutins: Optional[List[IngameCutin]]
    ingame_cutin_characters: Optional[List[IngameCutinCharacter]]
    ingame_judge_frames: Optional[List[IngameJudgeFrame]]
    ingame_note_judge_technical_scores: Optional[List[IngameNoteJudgeTechnicalScore]]
    shops: Optional[List[Shop]]
    shop_items: Optional[List[ShopItem]]
    costume3d_shop_items: Optional[List[Costume3dShopItem]]
    area_items: Optional[List[AreaItem]]
    area_item_levels: Optional[List[AreaItemLevel]]
    materials: Optional[List[Material]]
    gachas: Optional[List[Gacha]]
    gacha_bonuses: Optional[List[GachaBonus]]
    gacha_bonus_points: Optional[List[GachaBonusPoint]]
    gacha_extras: Optional[List[GachaExtra]]
    gift_gacha_exchanges: Optional[List[GiftGachaExchange]]
    gacha_tabs: Optional[List[Union[dict, str, int]]]
    practice_tickets: Optional[List[PracticeTicket]]
    skill_practice_tickets: Optional[List[SkillPracticeTicket]]
    levels: Optional[List[Level]]
    unit_stories: Optional[List[UnitStory]]
    special_stories: Optional[List[SpecialStory]]
    configs: Optional[List[Config]]
    client_configs: Optional[List[ClientConfig]]
    wordings: Optional[List[Wording]]
    costume3ds: Optional[List[Costume3d]]
    costume3d_models: Optional[List[Costume3dModel]]
    costume3d_model_available_patterns: Optional[List[Costume3dModelAvailablePattern]]
    game_character_unit3d_motions: Optional[List[GameCharacterUnit3dMotion]]
    costume2ds: Optional[List[Costume2d]]
    costume2d_groups: Optional[List[Costume2dGroup]]
    topics: Optional[List[Topic]]
    live_stages: Optional[List[LiveStage]]
    stamps: Optional[List[Stamp]]
    multi_live_lobbies: Optional[List[MultiLiveLobby]]
    master_lessons: Optional[List[MasterLesson]]
    master_lesson_rewards: Optional[List[MasterLessonReward]]
    card_exchange_resources: Optional[List[CardExchangeResource]]
    material_exchanges: Optional[List[MaterialExchange]]
    material_exchange_summaries: Optional[List[MaterialExchangeSummary]]
    boost_items: Optional[List[BoostItem]]
    billing_products: Optional[List[BillingProduct]]
    billing_shop_items: Optional[List[BillingShopItem]]
    billing_shop_item_exchange_costs: Optional[List[BillingShopItemExchangeCost]]
    colorful_passes: Optional[List[ColorfulPass]]
    jewel_behaviors: Optional[List[JewelBehavior]]
    character_ranks: Optional[List[CharacterRank]]
    character_mission_v2s: Optional[List[CharacterMissionV2]]
    character_mission_v2_parameter_groups: Optional[List[CharacterMissionV2ParameterGroup]]
    character_mission_v2_area_items: Optional[List[CharacterMissionV2AreaItem]]
    system_live2ds: Optional[List[SystemLive2d]]
    normal_missions: Optional[List[NormalMission]]
    beginner_missions: Optional[List[BeginnerMission]]
    resource_boxes: Optional[List[ResourceBox]]
    live_mission_periods: Optional[List[LiveMissionPeriod]]
    live_missions: Optional[List[LiveMission]]
    live_mission_passes: Optional[List[LiveMissionPass]]
    penlight_colors: Optional[List[PenlightColor]]
    penlights: Optional[List[Penlight]]
    live_talks: Optional[List[LiveTalk]]
    tips: Optional[List[Tip]]
    gacha_ceil_items: Optional[List[GachaCeilItem]]
    gacha_ceil_exchange_summaries: Optional[List[GachaCeilExchangeSummary]]
    player_rank_rewards: Optional[List[PlayerRankReward]]
    gacha_tickets: Optional[List[GachaTicket]]
    honor_groups: Optional[List[HonorGroup]]
    honors: Optional[List[Honor]]
    honor_missions: Optional[List[HonorMission]]
    bonds_honors: Optional[List[BondsHonor]]
    bonds_honor_words: Optional[List[BondsHonorWord]]
    bonds_rewards: Optional[List[BondsReward]]
    challenge_lives: Optional[List[ChallengeLive]]
    challenge_live_decks: Optional[List[ChallengeLiveDeck]]
    challenge_live_stages: Optional[List[ChallengeLiveStage]]
    challenge_live_stage_exs: Optional[List[ChallengeLiveStageEx]]
    challenge_live_high_score_rewards: Optional[List[ChallengeLiveHighScoreReward]]
    challenge_live_characters: Optional[List[ChallengeLiveCharacter]]
    challenge_live_play_day_reward_periods: Optional[List[ChallengeLivePlayDayRewardPeriod]]
    virtual_lives: Optional[List[VirtualLive]]
    virtual_shops: Optional[List[VirtualShop]]
    virtual_items: Optional[List[VirtualItem]]
    virtual_live_cheer_messages: Optional[List[VirtualLiveCheerMessage]]
    virtual_live_cheer_message_display_limits: Optional[
        List[VirtualLiveCheerMessageDisplayLimit]
    ]
    virtual_live_tickets: Optional[List[VirtualLiveTicket]]
    virtual_live_pamphlets: Optional[List[VirtualLivePamphlet]]
    avatar_accessories: Optional[List[AvatarAccessory]]
    avatar_costumes: Optional[List[AvatarCostume]]
    avatar_motions: Optional[List[AvatarMotion]]
    avatar_skin_colors: Optional[List[AvatarSkinColor]]
    avatar_coordinates: Optional[List[AvatarCoordinate]]
    ng_words: Optional[List[NgWord]]
    rule_slides: Optional[List[RuleSlide]]
    facilities: Optional[List[Facility]]
    one_time_behaviors: Optional[List[OneTimeBehavior]]
    login_bonuses: Optional[List[LoginBonus]]
    beginner_login_bonuses: Optional[List[BeginnerLoginBonus]]
    beginner_login_bonus_summaries: Optional[List[BeginnerLoginBonusSummary]]
    limited_login_bonuses: Optional[List[LimitedLoginBonus]]
    login_bonus_live2ds: Optional[List[LoginBonusLive2d]]
    events: Optional[List[Event]]
    event_musics: Optional[List[EventMusic]]
    event_deck_bonuses: Optional[List[EventDeckBonus]]
    event_rarity_bonus_rates: Optional[List[EventRarityBonusRate]]
    event_items: Optional[List[EventItem]]
    event_stories: Optional[List[EventStory]]
    event_exchange_summaries: Optional[List[EventExchangeSummary]]
    event_story_units: Optional[List[EventStoryUnit]]
    event_cards: Optional[List[EventCard]]
    preliminary_tournaments: Optional[List[PreliminaryTournament]]
    cheerful_carnival_summaries: Optional[List[CheerfulCarnivalSummary]]
    cheerful_carnival_teams: Optional[List[CheerfulCarnivalTeam]]
    cheerful_carnival_party_names: Optional[List[CheerfulCarnivalPartyName]]
    cheerful_carnival_character_party_names: Optional[
        List[CheerfulCarnivalCharacterPartyName]
    ]
    cheerful_carnival_live_team_point_bonuses: Optional[
        List[CheerfulCarnivalLiveTeamPointBonus]
    ]
    cheerful_carnival_rewards: Optional[List[CheerfulCarnivalReward]]
    cheerful_carnival_result_rewards: Optional[List[CheerfulCarnivalResultReward]]
    appeals: Optional[List[Appeal]]
    boosts: Optional[List[Boost]]
    boost_presents: Optional[List[BoostPresent]]
    boost_present_costs: Optional[List[BoostPresentCost]]
    episode_characters: Optional[List[EpisodeCharacter]]
    custom_profile_text_colors: Optional[List[CustomProfileTextColor]]
    custom_profile_text_fonts: Optional[List[CustomProfileTextFont]]
    custom_profile_player_info_resources: Optional[List[CustomProfilePlayerInfoResource]]
    custom_profile_general_background_resources: Optional[
        List[CustomProfileGeneralBackgroundResource]
    ]
    custom_profile_story_background_resources: Optional[
        List[CustomProfileStoryBackgroundResource]
    ]
    custom_profile_collection_resources: Optional[List[CustomProfileCollectionResource]]
    custom_profile_member_standing_picture_resources: Optional[
        List[CustomProfileMemberStandingPictureResource]
    ]
    custom_profile_shape_resources: Optional[List[CustomProfileShapeResource]]
    custom_profile_etc_resources: Optional[List[CustomProfileEtcResource]]
    custom_profile_member_resource_exclude_cards: Optional[List[Union[dict, str, int]]]
    custom_profile_gachas: Optional[List[CustomProfileGacha]]
    custom_profile_gacha_tabs: Optional[List[Union[dict, str, int]]]
    streaming_live_bgms: Optional[List[StreamingLiveBgm]]
    omikujis: Optional[List[Omikuji]]
    omikuji_groups: Optional[List[OmikujiGroup]]
    omikuji_rates: Optional[List[OmikujiRate]]
    omikuji_costs: Optional[List[OmikujiCost]]
    omikuji_rewards: Optional[List[OmikujiReward]]
    virtual_booth_shops: Optional[List[VirtualBoothShop]]
    special_seasons: Optional[List[SpecialSeason]]
    special_season_areas: Optional[List[SpecialSeasonArea]]
    rank_match_penalties: Optional[List[RankMatchPenalty]]
    rank_match_placements: Optional[List[RankMatchPlacement]]
    rank_match_bonus_point_conditions: Optional[List[RankMatchBonusPointCondition]]
    rank_match_seasons: Optional[List[RankMatchSeason]]
    rank_match_tiers: Optional[List[RankMatchTier]]
    rank_match_tier_bonus_points: Optional[List[RankMatchTierBonusPoint]]
    rank_match_grades: Optional[List[RankMatchGrade]]
    rank_match_classes: Optional[List[RankMatchClass]]
    limited_title_screens: Optional[List[LimitedTitleScreen]]
    panel_mission_campaigns: Optional[List[Union[dict, str, int]]]
