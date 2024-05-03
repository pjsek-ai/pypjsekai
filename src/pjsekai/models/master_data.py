# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from typing import List, Optional, Union
from pydantic import Field

from pjsekai.enums import *
from .model import Model


class GameCharacter(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    resource_id: Optional[int] = None
    first_name: Optional[str] = None
    given_name: Optional[str] = None
    first_name_ruby: Optional[str] = None
    given_name_ruby: Optional[str] = None
    gender: Optional[Union[Gender, Unknown]] = None
    height: Optional[float] = None
    live2d_height_adjustment: Optional[float] = None
    figure: Optional[Union[Figure, Unknown]] = None
    breast_size: Optional[Union[BreastSize, Unknown]] = None
    model_name: Optional[str] = None
    unit: Optional[Union[Unit, Unknown]] = None
    support_unit_type: Optional[Union[SupportUnitType, Unknown]] = None


class GameCharacterUnit(Model):
    id: Optional[int] = None
    game_character_id: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None
    color_code: Optional[str] = None
    skin_color_code: Optional[str] = None
    skin_shadow_color_code1: Optional[str] = None
    skin_shadow_color_code2: Optional[str] = None


class OutsideCharacter(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None


class Character3d(Model):
    id: Optional[int] = None
    character_type: Optional[Union[CharacterType, Unknown]] = None
    character_id: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None
    name: Optional[str] = None
    head_costume3d_id: Optional[int] = None
    hair_costume3d_id: Optional[int] = None
    body_costume3d_id: Optional[int] = None


class Character2d(Model):
    id: Optional[int] = None
    character_type: Optional[Union[CharacterType, Unknown]] = None
    character_id: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None
    asset_name: Optional[str] = None
    is_next_grade: Optional[bool] = None
    is_enabled_flip_display: Optional[bool] = None


class CharacterProfile(Model):
    character_id: Optional[int] = None
    character_voice: Optional[str] = None
    birthday: Optional[str] = None
    height: Optional[str] = None
    school: Optional[str] = None
    school_year: Optional[str] = None
    hobby: Optional[str] = None
    special_skill: Optional[str] = None
    favorite_food: Optional[str] = None
    hated_food: Optional[str] = None
    weak: Optional[str] = None
    introduction: Optional[str] = None
    scenario_id: Optional[str] = None


class Bond(Model):
    id: Optional[int] = None
    group_id: Optional[int] = None
    character_id1: Optional[int] = None
    character_id2: Optional[int] = None


class Live2d(Model):
    id: Optional[int] = None
    character_id: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None
    asset_bundle_name: Optional[str] = None
    motion: Optional[str] = None
    expression: Optional[str] = None
    weight: Optional[int] = None


class BondsLive2d(Live2d):
    default_flg: Optional[bool] = None


class BondsRankUpLive2d(Live2d):
    default_flg: Optional[bool] = None


class UnitProfile(Model):
    unit: Optional[Union[Unit, Unknown]] = None
    unit_name: Optional[str] = None
    seq: Optional[int] = None
    profile_sentence: Optional[str] = None
    color_code: Optional[str] = None
    unit_profile_name: Optional[str] = None


class ActionSet(Model):
    id: Optional[int] = None
    area_id: Optional[int] = None
    script_id: Optional[str] = None
    character_ids: Optional[List[int]] = None
    archive_display_type: Optional[Union[ArchiveDisplayType, Unknown]] = None
    archive_published_at: Optional[datetime] = None
    release_condition_id: Optional[int] = None
    scenario_id: Optional[str] = None
    action_set_type: Optional[Union[ActionSetType, Unknown]] = None
    special_season_id: Optional[int] = None
    is_next_grade: Optional[bool] = None


class Area(Model):
    id: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    area_type: Optional[Union[AreaType, Unknown]] = None
    view_type: Optional[Union[ViewType, Unknown]] = None
    name: Optional[str] = None
    release_condition_id: Optional[int] = None
    label: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    is_base_area: Optional[bool] = None
    display_timeline_type: Optional[Union[DisplayTimelineType, Unknown]] = None
    group_id: Optional[int] = None
    sub_name: Optional[str] = None
    additional_area_type: Optional[Union[AdditionalAreaType, Unknown]] = None


class AreaPlaylist(Model):
    id: Optional[int] = None
    area_id: Optional[int] = None
    music_id: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    bgm_name: Optional[str] = None
    release_condition_id: Optional[int] = None


class MobCharacter(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    gender: Optional[Union[Gender, Unknown]] = None


class CharacterCostume(Model):
    id: Optional[int] = None
    character_id: Optional[int] = None
    costume_id: Optional[int] = None
    sd_asset_bundle_name: Optional[str] = None
    live2d_asset_bundle_name: Optional[str] = None


class CardCostume3d(Model):
    card_id: Optional[int] = None
    costume3d_id: Optional[int] = None


class CardParameter(Model):
    id: Optional[int] = None
    card_id: Optional[int] = None
    card_level: Optional[int] = None
    card_parameter_type: Optional[Union[CardParameterType, Unknown]] = None
    power: Optional[int] = None


class Cost(Model):
    resource_id: Optional[int] = None
    resource_type: Optional[Union[ResourceType, Unknown]] = None
    resource_level: Optional[int] = None
    resource_quantity: Optional[int] = None
    quantity: Optional[int] = None


class SpecialTrainingCost(Model):
    card_id: Optional[int] = None
    seq: Optional[int] = None
    cost: Optional[Cost] = None


class MasterLessonAchieveResource(Model):
    release_condition_id: Optional[int] = None
    card_id: Optional[int] = None
    master_rank: Optional[int] = None
    resources: Optional[List] = None


class Card(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    character_id: Optional[int] = None
    card_rarity_type: Optional[Union[CardRarityType, Unknown]] = None
    special_training_power1_bonus_fixed: Optional[int] = None
    special_training_power2_bonus_fixed: Optional[int] = None
    special_training_power3_bonus_fixed: Optional[int] = None
    attr: Optional[Union[CardAttr, Unknown]] = None
    support_unit: Optional[Union[Unit, Unknown]] = None
    skill_id: Optional[int] = None
    card_skill_name: Optional[str] = None
    prefix: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    gacha_phrase: Optional[str] = None
    flavor_text: Optional[str] = None
    release_at: Optional[datetime] = None
    archive_published_at: Optional[datetime] = None
    card_parameters: Optional[List[CardParameter]] = None
    special_training_costs: Optional[List[SpecialTrainingCost]] = None
    master_lesson_achieve_resources: Optional[
        List[MasterLessonAchieveResource]
    ] = None
    archive_display_type: Optional[Union[ArchiveDisplayType, Unknown]] = None


class SkillEffectDetail(Model):
    id: Optional[int] = None
    level: Optional[int] = None
    activate_effect_duration: Optional[float] = None
    activate_effect_value_type: Optional[Union[ActivateEffectValueType, Unknown]] = None
    activate_effect_value: Optional[int] = None


class SkillEnhanceCondition(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None


class SkillEnhance(Model):
    id: Optional[int] = None
    skill_enhance_type: Optional[Union[SkillEnhanceType, Unknown]] = None
    activate_effect_value_type: Optional[Union[ActivateEffectValueType, Unknown]] = None
    activate_effect_value: Optional[int] = None
    skill_enhance_condition: Optional[SkillEnhanceCondition] = None


class SkillEffect(Model):
    id: Optional[int] = None
    skill_effect_type: Optional[Union[SkillEffectType, Unknown]] = None
    activate_notes_judgment_type: Optional[Union[IngameNoteJudgeType, Unknown]] = None
    skill_effect_details: Optional[List[SkillEffectDetail]] = None
    activate_life: Optional[int] = None
    condition_type: Optional[Union[SkillEffectConditionType, Unknown]] = None
    skill_enhance: Optional[SkillEnhance] = None


class Skill(Model):
    id: Optional[int] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    description_sprite_name: Optional[str] = None
    skill_filter_id: Optional[int] = None
    skill_effects: Optional[List[SkillEffect]] = None


class CardEpisode(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    card_id: Optional[int] = None
    title: Optional[str] = None
    scenario_id: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    release_condition_id: Optional[int] = None
    power1_bonus_fixed: Optional[int] = None
    power2_bonus_fixed: Optional[int] = None
    power3_bonus_fixed: Optional[int] = None
    reward_resource_box_ids: Optional[List[int]] = None
    costs: Optional[List[Cost]] = None
    card_episode_part_type: Optional[Union[CardEpisodePartType, Unknown]] = None


class CardRarity(Model):
    card_rarity_type: Optional[Union[CardRarityType, Unknown]] = None
    seq: Optional[int] = None
    max_level: Optional[int] = None
    max_skill_level: Optional[int] = None
    training_max_level: Optional[int] = None


class CardSkillCost(Model):
    id: Optional[int] = None
    material_id: Optional[int] = None
    exp: Optional[int] = None


class Music(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    release_condition_id: Optional[int] = None
    categories: Optional[List[Union[MusicCategory, Unknown]]] = None
    title: Optional[str] = None
    pronunciation: Optional[str] = None
    creator: Optional[str] = None
    lyricist: Optional[str] = None
    composer: Optional[str] = None
    arranger: Optional[str] = None
    dancer_count: Optional[int] = None
    self_dancer_position: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    live_talk_background_asset_bundle_name: Optional[str] = None
    published_at: Optional[datetime] = None
    live_stage_id: Optional[int] = None
    filler_sec: Optional[float] = None
    music_collaboration_id: Optional[int] = None
    creator_artist_id: Optional[int] = None
    is_newly_written_music: Optional[bool] = None
    released_at: Optional[datetime] = None
    is_full_length: Optional[bool] = None


class MusicTag(Model):
    id: Optional[int] = None
    music_id: Optional[int] = None
    music_tag: Optional[str] = None
    seq: Optional[int] = None


class MusicDifficulty(Model):
    id: Optional[int] = None
    music_id: Optional[int] = None
    music_difficulty: Optional[Union[MusicDifficultyType, Unknown]] = None
    play_level: Optional[int] = None
    release_condition_id: Optional[int] = None
    total_note_count: Optional[int] = None


class Character(Model):
    id: Optional[int] = None
    music_id: Optional[int] = None
    music_vocal_id: Optional[int] = None
    character_type: Optional[Union[CharacterType, Unknown]] = None
    character_id: Optional[int] = None
    seq: Optional[int] = None


class MusicVocal(Model):
    id: Optional[int] = None
    music_id: Optional[int] = None
    music_vocal_type: Optional[Union[MusicVocalType, Unknown]] = None
    seq: Optional[int] = None
    release_condition_id: Optional[int] = None
    caption: Optional[str] = None
    characters: Optional[List[Character]] = None
    asset_bundle_name: Optional[str] = None
    archive_published_at: Optional[datetime] = None
    special_season_id: Optional[int] = None
    archive_display_type: Optional[Union[ArchiveDisplayType, Unknown]] = None


class MusicDanceMember(Model):
    id: Optional[int] = None
    music_id: Optional[int] = None
    default_music_type: Optional[Union[DefaultMusicType, Unknown]] = None
    character_id1: Optional[int] = None
    unit1: Optional[Union[Unit, Unknown]] = None
    character_id2: Optional[int] = None
    unit2: Optional[Union[Unit, Unknown]] = None
    character_id3: Optional[int] = None
    unit3: Optional[Union[Unit, Unknown]] = None
    character_id4: Optional[int] = None
    unit4: Optional[Union[Unit, Unknown]] = None
    character_id5: Optional[int] = None
    unit5: Optional[Union[Unit, Unknown]] = None


class MusicAchievement(Model):
    id: Optional[int] = None
    music_achievement_type: Optional[Union[MusicAchievementType, Unknown]] = None
    music_achievement_type_value: Optional[str] = None
    resource_box_id: Optional[int] = None
    music_difficulty_type: Optional[Union[MusicDifficultyType, Unknown]] = None


class MusicVideoCharacter(Model):
    id: Optional[int] = None
    music_id: Optional[int] = None
    default_music_type: Optional[Union[DefaultMusicType, Unknown]] = None
    game_character_unit_id: Optional[int] = None
    dance_priority: Optional[int] = None
    seq: Optional[int] = None
    priority: Optional[int] = None


class MusicAssetVariant(Model):
    id: Optional[int] = None
    music_vocal_id: Optional[int] = None
    seq: Optional[int] = None
    music_asset_type: Optional[Union[MusicAssetType, Unknown]] = None
    asset_bundle_name: Optional[str] = None


class MusicCollaboration(Model):
    id: Optional[int] = None
    label: Optional[str] = None


class EpisodeMusicVideoCostume(Model):
    id: Optional[int] = None
    music_vocal_id: Optional[int] = None
    character3d_id1: Optional[int] = None
    character3d_id2: Optional[int] = None
    character3d_id3: Optional[int] = None
    character3d_id4: Optional[int] = None
    character3d_id5: Optional[int] = None


class MusicOriginal(Model):
    id: Optional[int] = None
    music_id: Optional[int] = None
    video_link: Optional[str] = None


class ReleaseCondition(Model):
    id: Optional[int] = None
    sentence: Optional[str] = None
    release_condition_type: Optional[Union[ReleaseConditionType, Unknown]] = None
    release_condition_type_level: Optional[int] = None
    release_condition_type_id: Optional[int] = None
    release_condition_type_quantity: Optional[int] = None
    release_condition_type_id2: Optional[int] = None


class PlayLevelScore(Model):
    live_type: Optional[Union[LiveType, Unknown]] = None
    play_level: Optional[int] = None
    s: Optional[int] = None
    a: Optional[int] = None
    b: Optional[int] = None
    c: Optional[int] = None


class IngameCombo(Model):
    id: Optional[int] = None
    from_count: Optional[int] = None
    to_count: Optional[int] = None
    score_coefficient: Optional[float] = None


class IngameNote(Model):
    id: Optional[int] = None
    ingame_note_type: Optional[Union[IngameNoteType, Unknown]] = None
    score_coefficient: Optional[float] = None
    damage_bad: Optional[int] = None
    damage_miss: Optional[int] = None


class IngameNoteJudge(Model):
    id: Optional[int] = None
    ingame_note_jadge_type: Optional[Union[IngameNoteJudgeType, Unknown]] = None
    score_coefficient: Optional[float] = None
    damage: Optional[int] = None


class IngamePlayLevel(Model):
    play_level: Optional[int] = None
    score_coefficient: Optional[float] = None


class IngameCutin(Model):
    id: Optional[int] = None
    music_difficulty: Optional[Union[MusicDifficultyType, Unknown]] = None
    combo: Optional[int] = None


class IngameCutinCharacter(Model):
    id: Optional[int] = None
    ingame_cutin_character_type: Optional[Union[IngameCutinCharacterType, Unknown]] = None
    priority: Optional[int] = None
    game_character_unit_id1: Optional[int] = None
    game_character_unit_id2: Optional[int] = None
    asset_bundle_name1: Optional[str] = None
    asset_bundle_name2: Optional[str] = None
    release_condition_id: Optional[int] = None
    is_lottery_target: Optional[bool] = None
    first_character_archive_voice_id: Optional[int] = None
    second_character_archive_voice_id: Optional[int] = None


class IngameJudgeFrame(Model):
    id: Optional[int] = None
    ingame_note_type: Optional[Union[IngameNoteType, Unknown]] = None
    perfect: Optional[float] = None
    great: Optional[float] = None
    good: Optional[float] = None
    bad: Optional[float] = None
    perfect_before: Optional[float] = None
    perfect_after: Optional[float] = None
    great_before: Optional[float] = None
    great_after: Optional[float] = None
    good_before: Optional[float] = None
    good_after: Optional[float] = None
    bad_before: Optional[float] = None
    bad_after: Optional[float] = None


class IngameNoteJudgeTechnicalScore(Model):
    id: Optional[int] = None
    live_type: Optional[Union[LiveType, Unknown]] = None
    ingame_note_jadge_type: Optional[Union[IngameNoteJudgeType, Unknown]] = None
    score: Optional[int] = None


class Shop(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    shop_type: Optional[Union[ShopType, Unknown]] = None
    area_id: Optional[int] = None
    name: Optional[str] = None
    release_condition_id: Optional[int] = None


class ShopItemCost(Model):
    shop_item_id: Optional[int] = None
    seq: Optional[int] = None
    cost: Optional[Cost] = None


class ShopItem(Model):
    id: Optional[int] = None
    shop_id: Optional[int] = None
    seq: Optional[int] = None
    release_condition_id: Optional[int] = None
    resource_box_id: Optional[int] = None
    costs: Optional[List[ShopItemCost]] = None
    start_at: Optional[datetime] = None


class Costume3dShopItemCost(Cost):
    id: Optional[int] = None
    costume3d_shop_item_id: Optional[int] = None
    seq: Optional[int] = None


class Costume3dShopItem(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    group_id: Optional[int] = None
    name: Optional[str] = None
    body_costume3d_id: Optional[int] = None
    release_condition_id: Optional[int] = None
    costs: Optional[List[Costume3dShopItemCost]] = None
    start_at: Optional[datetime] = None
    head_costume3d_id: Optional[int] = None


class AreaItem(Model):
    id: Optional[int] = None
    area_id: Optional[int] = None
    name: Optional[str] = None
    flavor_text: Optional[str] = None
    spawn_point: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class AreaItemLevel(Model):
    area_item_id: Optional[int] = None
    level: Optional[int] = None
    target_unit: Optional[Union[Unit, Unknown]] = None
    target_card_attr: Optional[Union[CardAttr, Unknown]] = None
    target_game_character_id: Optional[int] = None
    power1_bonus_rate: Optional[float] = None
    power1_all_match_bonus_rate: Optional[float] = None
    power2_bonus_rate: Optional[float] = None
    power2_all_match_bonus_rate: Optional[float] = None
    power3_bonus_rate: Optional[float] = None
    power3_all_match_bonus_rate: Optional[float] = None
    sentence: Optional[str] = None


class Material(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    flavor_text: Optional[str] = None
    material_type: Optional[Union[MaterialType, Unknown]] = None


class GachaCardRarityRate(Model):
    id: Optional[int] = None
    group_id: Optional[int] = None
    card_rarity_type: Optional[Union[CardRarityType, Unknown]] = None
    lottery_type: Optional[Union[LotteryType, Unknown]] = None
    rate: Optional[float] = None


class GachaDetail(Model):
    id: Optional[int] = None
    gacha_id: Optional[int] = None
    card_id: Optional[int] = None
    weight: Optional[int] = None
    is_wish: Optional[bool] = None
    gacha_detail_wish_type: Optional[Union[GachaDetailWishType, Unknown]] = None
    fixed_bonus_weight: Optional[int] = None


class GachaBehavior(Model):
    id: Optional[int] = None
    gacha_id: Optional[int] = None
    gacha_behavior_type: Optional[Union[GachaBehaviorType, Unknown]] = None
    cost_resource_type: Optional[Union[ResourceType, Unknown]] = None
    cost_resource_quantity: Optional[int] = None
    spin_count: Optional[int] = None
    execute_limit: Optional[int] = None
    group_id: Optional[int] = None
    priority: Optional[int] = None
    resource_category: Optional[Union[ResourceCategory, Unknown]] = None
    gacha_spinnable_type: Optional[Union[GachaSpinnableType, Unknown]] = None
    cost_resource_id: Optional[int] = None
    gacha_extra_id: Optional[int] = None


class GachaPickup(Model):
    id: Optional[int] = None
    gacha_id: Optional[int] = None
    card_id: Optional[int] = None
    gacha_pickup_type: Optional[Union[GachaPickupType, Unknown]] = None


class GachaInformation(Model):
    gacha_id: Optional[int] = None
    summary: Optional[str] = None
    description: Optional[str] = None


class Gacha(Model):
    id: Optional[int] = None
    gacha_type: Optional[Union[GachaType, Unknown]] = None
    name: Optional[str] = None
    seq: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    gacha_card_rarity_rate_group_id: Optional[int] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    is_show_period: Optional[bool] = None
    gacha_ceil_item_id: Optional[int] = None
    wish_select_count: Optional[int] = None
    wish_fixed_select_count: Optional[int] = None
    wish_limited_select_count: Optional[int] = None
    gacha_card_rarity_rates: Optional[List[GachaCardRarityRate]] = None
    gacha_details: Optional[List[GachaDetail]] = None
    gacha_behaviors: Optional[List[GachaBehavior]] = None
    gacha_pickups: Optional[List[GachaPickup]] = None
    gacha_pickup_costumes: Optional[List] = None
    gacha_information: Optional[GachaInformation] = None
    drawable_gacha_hour: Optional[int] = None
    gacha_bonus_id: Optional[int] = None
    spin_limit: Optional[int] = None


class GachaBonus(Model):
    id: Optional[int] = None
    switch_fixed_bonus_weight: Optional[bool] = None


class GachaBonusPoint(Model):
    id: Optional[int] = None
    resource_type: Optional[Union[ResourceType, Unknown]] = None
    point: Optional[float] = None


class GachaExtra(Model):
    id: Optional[int] = None
    resource_box_id: Optional[int] = None


class GiftGachaExchange(Model):
    id: Optional[int] = None
    gacha_id: Optional[int] = None
    seq: Optional[int] = None
    resource_box_id: Optional[int] = None


class GachaTab(Model):
    id: Optional[int] = None
    child_gacha_ids: Optional[List[int]] = None
    seq: Optional[int] = None
    asset_bundle_name: Optional[str] = None


class PracticeTicket(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    exp: Optional[int] = None
    flavor_text: Optional[str] = None


class SkillPracticeTicket(PracticeTicket):
    pass


class Level(Model):
    id: Optional[int] = None
    level_type: Optional[Union[LevelType, Unknown]] = None
    level: Optional[int] = None
    total_exp: Optional[int] = None


class Episode(Model):
    id: Optional[int] = None
    episode_no: Optional[int] = None
    title: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    scenario_id: Optional[str] = None
    release_condition_id: Optional[int] = None
    reward_resource_box_ids: Optional[List[int]] = None


class UnitStoryEpisode(Episode):
    unit: Optional[Union[Unit, Unknown]] = None
    chapter_no: Optional[int] = None
    unit_episode_category: Optional[Union[Unit, Unknown]] = None
    episode_no_label: Optional[str] = None
    limited_release_start_at: Optional[datetime] = None
    limited_release_end_at: Optional[datetime] = None
    and_release_condition_id: Optional[int] = None
    unit_story_episode_group_id: Optional[int] = None


class Chapter(Model):
    id: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None
    chapter_no: Optional[int] = None
    title: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    episodes: Optional[List[UnitStoryEpisode]] = None


class UnitStory(Model):
    unit: Optional[Union[Unit, Unknown]] = None
    seq: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    chapters: Optional[List[Chapter]] = None


class SpecialStoryEpisode(Episode):
    special_story_id: Optional[int] = None
    special_story_episode_type: Optional[str] = None
    is_able_skip: Optional[bool] = None
    is_action_set_refresh: Optional[bool] = None
    special_story_episode_type_id: Optional[int] = None


class SpecialStory(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    title: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    episodes: Optional[List[SpecialStoryEpisode]] = None


class Config(Model):
    config_key: Optional[str] = None
    value: Optional[str] = None


class ClientConfig(Model):
    id: Optional[int] = None
    value: Optional[str] = None
    type: Optional[Union[ClientConfigType, Unknown]] = None


class Wording(Model):
    wording_key: Optional[str] = None
    value: Optional[str] = None


class Costume3d(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    costume3d_group_id: Optional[int] = None
    costume3d_type: Optional[Union[Costume3dType, Unknown]] = None
    name: Optional[str] = None
    part_type: Optional[Union[PartType, Unknown]] = None
    color_id: Optional[int] = None
    color_name: Optional[str] = None
    character_id: Optional[int] = None
    costume3d_rarity: Optional[Union[Costume3dRarity, Unknown]] = None
    how_to_obtain: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    designer: Optional[str] = None
    archive_display_type: Optional[Union[ArchiveDisplayType, Unknown]] = None
    archive_published_at: Optional[datetime] = None
    published_at: Optional[datetime] = None


class Costume3dModel(Model):
    id: Optional[int] = None
    costume3d_id: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None
    head_costume3d_asset_bundle_type: Optional[Union[HeadCostume3dAssetBundleType, Unknown]] = None
    thumbnail_asset_bundle_name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    color_asset_bundle_name: Optional[str] = None
    part: Optional[str] = None


class Costume3dModelAvailablePattern(Model):
    id: Optional[int] = None
    head_costume3d_id: Optional[int] = None
    hair_costume3d_id: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None
    is_default: Optional[bool] = None


class GameCharacterUnit3dMotion(Model):
    id: Optional[int] = None
    game_character_unit_id: Optional[int] = None
    motion_type: Optional[Union[MotionType, Unknown]] = None
    asset_bundle_name: Optional[str] = None


class Costume2d(Model):
    id: Optional[int] = None
    costume2d_group_id: Optional[int] = None
    character2d_id: Optional[int] = None
    from_mmddhh: Optional[str] = None
    to_mmddhh: Optional[str] = None
    live2d_asset_bundle_name: Optional[str] = None
    spine_asset_bundle_name: Optional[str] = None


class Costume2dGroup(Model):
    id: Optional[int] = None
    name: Optional[str] = None


class Topic(Model):
    id: Optional[int] = None
    topic_type: Optional[Union[TopicType, Unknown]] = None
    topic_type_id: Optional[int] = None
    release_condition_id: Optional[int] = None


class LiveStage(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class Stamp(Model):
    id: Optional[int] = None
    stamp_type: Optional[Union[StampType, Unknown]] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    balloon_asset_bundle_name: Optional[str] = None
    character_id1: Optional[int] = None
    game_character_unit_id: Optional[int] = None
    archive_published_at: Optional[datetime] = None
    description: Optional[str] = None
    archive_display_type: Optional[Union[ArchiveDisplayType, Unknown]] = None
    character_id2: Optional[int] = None


class MultiLiveLobby(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    photon_lobby_name: Optional[str] = None
    matching_logic: Optional[Union[MatchingLogic, Unknown]] = None
    total_power: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    multi_live_lobby_type: Optional[Union[MultiLiveLobbyType, Unknown]] = None


class MasterLessonCost(Cost):
    id: Optional[int] = None
    card_rarity_type: Optional[Union[CardRarityType, Unknown]] = None
    master_rank: Optional[int] = None
    seq: Optional[int] = None


class MasterLesson(Model):
    card_rarity_type: Optional[Union[CardRarityType, Unknown]] = None
    master_rank: Optional[int] = None
    power1_bonus_fixed: Optional[int] = None
    power2_bonus_fixed: Optional[int] = None
    power3_bonus_fixed: Optional[int] = None
    character_rank_exp: Optional[int] = None
    costs: Optional[List[MasterLessonCost]] = None
    rewards: Optional[List] = None


class MasterLessonReward(Model):
    id: Optional[int] = None
    card_id: Optional[int] = None
    master_rank: Optional[int] = None
    seq: Optional[int] = None
    resource_box_id: Optional[int] = None
    card_rarity: Optional[int] = None


class CardExchangeResource(Model):
    card_rarity_type: Optional[Union[CardRarityType, Unknown]] = None
    seq: Optional[int] = None
    resource_box_id: Optional[int] = None


class MaterialExchangeCost(Cost):
    material_exchange_id: Optional[int] = None
    cost_group_id: Optional[int] = None
    seq: Optional[int] = None


class MaterialExchange(Model):
    id: Optional[int] = None
    material_exchange_summary_id: Optional[int] = None
    seq: Optional[int] = None
    resource_box_id: Optional[int] = None
    refresh_cycle: Optional[Union[RefreshCycle, Unknown]] = None
    costs: Optional[List[MaterialExchangeCost]] = None
    exchange_limit: Optional[int] = None
    start_at: Optional[datetime] = None
    is_display_quantity: Optional[bool] = None
    display_name: Optional[str] = None
    thumbnail_asset_bundle_name: Optional[str] = None


class MaterialExchangeSummary(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    exchange_category: Optional[Union[ExchangeCategory, Unknown]] = None
    material_exchange_type: Optional[Union[MaterialExchangeType, Unknown]] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    start_at: Optional[datetime] = None
    material_exchanges: Optional[List[MaterialExchange]] = None
    end_at: Optional[datetime] = None
    notification_remain_hour: Optional[int] = None


class BoostItem(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    recovery_value: Optional[int] = None
    asset_bundle_name: Optional[str] = Field(None, alias="assetBundleName")
    flavor_text: Optional[str] = None


class BillingProduct(Model):
    id: Optional[int] = None
    group_id: Optional[int] = None
    platform: Optional[Platform] = None
    product_id: Optional[str] = None
    price: Optional[int] = None
    unit_price: Optional[float] = None


class BillingShopItem(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    billing_shop_item_type: Optional[Union[BillingShopItemType, Unknown]] = None
    billing_product_group_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    billable_limit_type: Optional[Union[BillableLimitType, Unknown]] = None
    billable_limit_reset_interval_type: Optional[Union[BillableLimitResetIntervalType, Unknown]] = None
    asset_bundle_name: Optional[str] = None
    resource_box_id: Optional[int] = None
    billable_limit_value: Optional[int] = None
    bonus_resource_box_id: Optional[int] = None
    label: Optional[str] = None
    end_at: Optional[datetime] = None
    start_at: Optional[datetime] = None
    billable_limit_reset_interval_value: Optional[int] = None
    purchase_option: Optional[Union[PurchaseOption, Unknown]] = None
    sale_type: Optional[str] = None


class BillingShopItemExchangeCost(Cost):
    id: Optional[int] = None
    billing_shop_item_id: Optional[int] = None


class BillingShopItemGroup(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    seq: Optional[int] = None
    billing_shop_item_ids: Optional[List[int]] = None


class ColorfulPass(Model):
    id: Optional[int] = None
    resource_box_id: Optional[int] = None
    receivable_days: Optional[int] = None
    present_sentence: Optional[str] = None
    expire_days: Optional[int] = None
    daily_paid_gacha_spin_limit: Optional[int] = None
    challenge_live_point_multiple: Optional[int] = None
    live_point_multiple: Optional[int] = None


class ColorfulPassV2(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    colorful_pass_tier: Optional[Union[ColorfulPassTier, Unknown]] = None
    resource_box_id: Optional[int] = None
    present_sentence: Optional[str] = None
    expire_days: Optional[int] = None
    challenge_live_point_rate: Optional[int] = None
    live_point_rate: Optional[int] = None
    daily_paid_gacha_spin_limit: Optional[int] = None
    daily_free_gacha_spin_limit: Optional[int] = None
    weekly_colorful_pass_gacha_spin_limit: Optional[int] = None
    is_priority_for_offline_event_entry: Optional[bool] = None
    max_live_bonus_count: Optional[int] = None
    max_auto_play_count: Optional[int] = None
    virtual_item_relation_group_id: Optional[int] = None
    virtual_live_cheer_message_relation_group_id: Optional[int] = None


class JewelBehavior(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    jewel_behavior_type: Optional[Union[JewelBehaviorType, Unknown]] = None
    jewel_behavior_type_quantity: Optional[int] = None
    amount: Optional[int] = None


class CharacterRankAchieveResource(Model):
    release_condition_id: Optional[int] = None
    character_id: Optional[int] = None
    character_rank: Optional[int] = None
    resources: Optional[List] = None


class CharacterRank(Model):
    id: Optional[int] = None
    character_id: Optional[int] = None
    character_rank: Optional[int] = None
    power1_bonus_rate: Optional[float] = None
    power2_bonus_rate: Optional[float] = None
    power3_bonus_rate: Optional[float] = None
    reward_resource_box_ids: Optional[List[int]] = None
    character_rank_achieve_resources: Optional[
        List[CharacterRankAchieveResource]
    ] = None


class CharacterMissionV2(Model):
    id: Optional[int] = None
    character_mission_type: Optional[Union[CharacterMissionType, Unknown]] = None
    character_id: Optional[int] = None
    parameter_group_id: Optional[int] = None
    sentence: Optional[str] = None
    progress_sentence: Optional[str] = None
    is_achievement_mission: Optional[bool] = None


class CharacterMissionV2ParameterGroup(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    requirement: Optional[int] = None
    exp: Optional[int] = None
    quantity: Optional[int] = None


class CharacterMissionV2AreaItem(Model):
    id: Optional[int] = None
    character_mission_type: Optional[Union[CharacterMissionType, Unknown]] = None
    area_item_id: Optional[int] = None
    character_id: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None


class SystemLive2d(Live2d):
    serif: Optional[str] = None
    voice: Optional[str] = None
    published_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    special_season_id: Optional[int] = None


class MissionReward(Model):
    id: Optional[int] = None
    mission_type: Optional[Union[MissionType, Unknown]] = None
    mission_id: Optional[int] = None
    seq: Optional[int] = None
    resource_box_id: Optional[int] = None


class NormalMission(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    normal_mission_type: Optional[Union[NormalMissionType, Unknown]] = None
    requirement: Optional[int] = None
    sentence: Optional[str] = None
    rewards: Optional[List[MissionReward]] = None


class BeginnerMission(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    beginner_mission_type: Optional[Union[BeginnerMissionType, Unknown]] = None
    beginner_mission_category: Optional[Union[BeginnerMissionCategory, Unknown]] = None
    condition_value: Optional[int] = None
    requirement: Optional[int] = None
    sentence: Optional[str] = None
    rewards: Optional[List[MissionReward]] = None


class Detail(Model):
    resource_box_purpose: Optional[Union[ResourceBoxPurpose, Unknown]] = None
    resource_box_id: Optional[int] = None
    seq: Optional[int] = None
    resource_type: Optional[Union[ResourceType, Unknown]] = None
    resource_quantity: Optional[int] = None
    resource_id: Optional[int] = None
    resource_level: Optional[int] = None


class ResourceBox(Model):
    resource_box_purpose: Optional[Union[ResourceBoxPurpose, Unknown]] = None
    id: Optional[int] = None
    resource_box_type: Optional[Union[ResourceBoxType, Unknown]] = None
    details: Optional[List[Detail]] = None
    description: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    name: Optional[str] = None


class LiveMissionPeriod(Model):
    id: Optional[int] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    sentence: Optional[str] = None


class LiveMission(Model):
    id: Optional[int] = None
    live_mission_period_id: Optional[int] = None
    live_mission_type: Optional[Union[LiveMissionType, Unknown]] = None
    requirement: Optional[int] = None
    rewards: Optional[List[MissionReward]] = None


class LiveMissionPass(Model):
    id: Optional[int] = None
    live_mission_period_id: Optional[int] = None
    costume_name: Optional[str] = None
    character3d_id1: Optional[int] = None
    character3d_id2: Optional[int] = None
    male_asset_bundle_name: Optional[str] = None
    female_asset_bundle_name: Optional[str] = None


class PenlightColor(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    color_code: Optional[str] = None
    character_id: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None


class Penlight(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    default_penlight_color_id: Optional[int] = None
    asset_bundle_name: Optional[str] = None


class LiveTalk(Model):
    id: Optional[int] = None
    live_talk_type: Optional[Union[LiveTalkType, Unknown]] = None
    scenario_id: Optional[str] = None
    character_id1: Optional[int] = None
    character_id2: Optional[int] = None


class Tip(Model):
    id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    from_user_rank: Optional[int] = None
    to_user_rank: Optional[int] = None
    asset_bundle_name: Optional[str] = None


class GachaCeilItem(Model):
    id: Optional[int] = None
    gacha_id: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    convert_start_at: Optional[datetime] = None
    convert_resource_box_id: Optional[int] = None


class GachaCeilExchangeCost(Cost):
    gacha_ceil_exchange_id: Optional[int] = None
    gacha_ceil_item_id: Optional[int] = None


class GachaCeilExchangeSubstituteCost(Cost):
    id: Optional[int] = None
    substitute_quantity: Optional[int] = None


class GachaCeilExchange(Model):
    id: Optional[int] = None
    gacha_ceil_exchange_summary_id: Optional[int] = None
    seq: Optional[int] = None
    resource_box_id: Optional[int] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    gacha_ceil_exchange_cost: Optional[GachaCeilExchangeCost] = None
    gacha_ceil_exchange_substitute_costs: Optional[
        List[GachaCeilExchangeSubstituteCost]
    ] = None
    exchange_limit: Optional[int] = None
    gacha_ceil_exchange_label_type: Optional[Union[GachaCeilExchangeLabelType, Unknown]] = None
    substitute_limit: Optional[int] = None


class GachaCeilExchangeSummary(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    gacha_id: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    gacha_ceil_exchanges: Optional[List[GachaCeilExchange]] = None
    gacha_ceil_item_id: Optional[int] = None


class PlayerRankReward(Model):
    id: Optional[int] = None
    player_rank: Optional[int] = None
    seq: Optional[int] = None
    resource_box_id: Optional[int] = None


class GachaTicket(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    gacha_display_type: Optional[Union[GachaDisplayType, Unknown]] = None


class HonorGroup(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    honor_type: Optional[Union[HonorType, Unknown]] = None
    background_asset_bundle_name: Optional[str] = None
    frame_name: Optional[str] = None


class HonorLevel(Model):
    honor_id: Optional[int] = None
    level: Optional[int] = None
    bonus: Optional[int] = None
    description: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    honor_rarity: Optional[Union[HonorRarity, Unknown]] = None


class Honor(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    group_id: Optional[int] = None
    honor_rarity: Optional[Union[HonorRarity, Unknown]] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    levels: Optional[List[HonorLevel]] = None
    honor_type_id: Optional[int] = None
    honor_mission_type: Optional[Union[HonorMissionType, Unknown]] = None


class HonorMission(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    honor_mission_type: Optional[Union[HonorMissionType, Unknown]] = None
    requirement: Optional[int] = None
    sentence: Optional[str] = None
    rewards: Optional[List[MissionReward]] = None


class BondsHonorLevel(Model):
    id: Optional[int] = None
    bonds_honor_id: Optional[int] = None
    level: Optional[int] = None
    description: Optional[str] = None


class BondsHonor(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    bonds_group_id: Optional[int] = None
    game_character_unit_id1: Optional[int] = None
    game_character_unit_id2: Optional[int] = None
    honor_rarity: Optional[Union[HonorRarity, Unknown]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    levels: Optional[List[BondsHonorLevel]] = None
    configurable_unit_virtual_singer: Optional[bool] = None


class BondsHonorWord(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    bonds_group_id: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None


class BondsReward(Model):
    id: Optional[int] = None
    bonds_group_id: Optional[int] = None
    rank: Optional[int] = None
    seq: Optional[int] = None
    bonds_reward_type: Optional[Union[BondsRewardType, Unknown]] = None
    resource_box_id: Optional[int] = None
    description: Optional[str] = None


class ChallengeLiveDetail(Model):
    id: Optional[int] = None
    challenge_live_id: Optional[int] = None
    challenge_live_type: Optional[Union[LiveType, Unknown]] = None


class ChallengeLive(Model):
    id: Optional[int] = None
    playable_count: Optional[int] = None
    challenge_live_details: Optional[List[ChallengeLiveDetail]] = None


class ChallengeLiveDeck(Model):
    id: Optional[int] = None
    character_id: Optional[int] = None
    release_condition_id: Optional[int] = None
    card_limit: Optional[int] = None


class ChallengeLiveStage(Model):
    id: Optional[int] = None
    character_id: Optional[int] = None
    rank: Optional[int] = None
    name: Optional[str] = None
    next_stage_challenge_point: Optional[int] = None
    complete_stage_resource_box_id: Optional[int] = None
    complete_stage_character_exp: Optional[int] = None


class ChallengeLiveStageEx(Model):
    id: Optional[int] = None
    character_id: Optional[int] = None
    from_rank: Optional[int] = None
    to_rank: Optional[int] = None
    name: Optional[str] = None
    next_stage_challenge_point: Optional[int] = None
    complete_stage_resource_box_id: Optional[int] = None
    complete_stage_character_exp: Optional[int] = None


class ChallengeLiveHighScoreReward(Model):
    id: Optional[int] = None
    character_id: Optional[int] = None
    high_score: Optional[int] = None
    resource_box_id: Optional[int] = None


class ChallengeLiveCharacter(Model):
    id: Optional[int] = None
    character_id: Optional[int] = None
    release_condition_id: Optional[int] = None
    or_release_condition_id: Optional[int] = None


class ChallengeLivePlayDayReward(Model):
    id: Optional[int] = None
    challenge_live_play_day_reward_period_id: Optional[int] = None
    play_days: Optional[int] = None
    seq: Optional[int] = None
    resource_box_id: Optional[int] = None


class ChallengeLivePlayDayRewardPeriod(Model):
    id: Optional[int] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    priority: Optional[int] = None
    challenge_live_play_day_rewards: Optional[List[ChallengeLivePlayDayReward]] = None


class VirtualLiveSetlist(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    seq: Optional[int] = None
    virtual_live_setlist_type: Optional[Union[VirtualLiveSetlistType, Unknown]] = None
    asset_bundle_name: Optional[str] = None
    virtual_live_stage_id: Optional[int] = None
    music_id: Optional[int] = None
    music_vocal_id: Optional[int] = None
    character3d_id1: Optional[int] = None
    character3d_id2: Optional[int] = None
    character3d_id3: Optional[int] = None
    character3d_id4: Optional[int] = None
    character3d_id5: Optional[int] = None
    character3d_id6: Optional[int] = None


class VirtualLiveBeginnerSchedule(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    day_of_week: Optional[Union[DayOfWeek, Unknown]] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None


class VirtualLiveSchedule(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    seq: Optional[int] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    notice_group_id: Optional[str] = None
    is_after_event: Optional[bool] = None


class VirtualLiveCharacter(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    game_character_unit_id: Optional[int] = None
    seq: Optional[int] = None
    virtual_live_performance_type: Optional[Union[VirtualLivePerformanceType, Unknown]] = None


class VirtualLiveReward(Model):
    id: Optional[int] = None
    virtual_live_type: Optional[Union[VirtualLiveType, Unknown]] = None
    virtual_live_id: Optional[int] = None
    resource_box_id: Optional[int] = None


class VirtualLiveWaitingRoom(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    lobby_asset_bundle_name: Optional[str] = None


class VirtualItem(Model):
    id: Optional[int] = None
    virtual_item_category: Optional[Union[VirtualItemCategory, Unknown]] = None
    seq: Optional[int] = None
    priority: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    cost_virtual_coin: Optional[int] = None
    cost_jewel: Optional[int] = None
    cheer_point: Optional[int] = None
    effect_asset_bundle_name: Optional[str] = None
    effect_expression_type: Optional[Union[EffectExpressionType, Unknown]] = None
    unit: Optional[Union[Unit, Unknown]] = None
    game_character_unit_id: Optional[int] = None
    virtual_item_label_type: Optional[Union[VirtualItemLabelType, Unknown]] = None


class VirtualLiveAppeal(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    virtual_live_stage_status: Optional[Union[VirtualLiveStageStatus, Unknown]] = None
    appeal_text: Optional[str] = None


class VirtualLiveBackgroundMusic(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    background_music_id: Optional[int] = None


class VirtualLiveInformation(Model):
    virtual_live_id: Optional[int] = None
    summary: Optional[str] = None
    description: Optional[str] = None


class VirtualLive(Model):
    id: Optional[int] = None
    virtual_live_type: Optional[Union[VirtualLiveType, Unknown]] = None
    virtual_live_platform: Optional[str] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    screen_mv_music_vocal_id: Optional[int] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    ranking_announce_at: Optional[datetime] = None
    virtual_live_setlists: Optional[List[VirtualLiveSetlist]] = None
    virtual_live_beginner_schedules: Optional[
        List[VirtualLiveBeginnerSchedule]
    ] = None
    virtual_live_schedules: Optional[List[VirtualLiveSchedule]] = None
    virtual_live_characters: Optional[List[VirtualLiveCharacter]] = None
    virtual_live_reward: Optional[VirtualLiveReward] = None
    virtual_live_rewards: Optional[List[VirtualLiveReward]] = None
    virtual_live_cheer_point_rewards: Optional[List] = None
    virtual_live_waiting_room: Optional[VirtualLiveWaitingRoom] = None
    virtual_items: Optional[List[VirtualItem]] = None
    virtual_live_appeals: Optional[List[VirtualLiveAppeal]] = None
    virtual_live_background_musics: Optional[List[VirtualLiveBackgroundMusic]] = None
    virtual_live_information: Optional[VirtualLiveInformation] = None
    archive_release_condition_id: Optional[int] = None
    virtual_live_ticket_id: Optional[int] = None


class VirtualShopItem(Model):
    id: Optional[int] = None
    virtual_shop_id: Optional[int] = None
    virtual_shop_item_type: Optional[Union[VirtualShopItemType, Unknown]] = None
    seq: Optional[int] = None
    resource_box_id: Optional[int] = None
    cost_virtual_coin: Optional[int] = None
    cost_jewel: Optional[int] = None
    start_at: Optional[datetime] = None
    cost_paid_jewel: Optional[int] = None
    end_at: Optional[datetime] = None
    limit_value: Optional[int] = None


class VirtualShop(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    virtual_shop_items: Optional[List[VirtualShopItem]] = None
    virtual_shop_type: Optional[Union[VirtualShopType, Unknown]] = None
    virtual_live_id: Optional[int] = None


class PaidVirtualLiveShopCost(Model):
    id: Optional[int] = None
    cost_resource_type: Optional[Union[ResourceType, Unknown]] = None
    cost_resource_quantity: Optional[int] = None
    start_at: Optional[datetime] = None


class PaidVirtualLiveShopItem(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    paid_virtual_live_shop_item_group_id: Optional[int] = None
    name: Optional[str] = None
    resource_box_id: Optional[int] = None
    paid_virtual_live_shop_item_purchase_type: Optional[
        Union[PaidVirtualLiveShopItemPurchaseType, Unknown]] = None
    paid_virtual_live_shop_costs: Optional[List[PaidVirtualLiveShopCost]] = None
    asset_bundle_name: Optional[str] = None
    description: Optional[str] = None


class PaidVirtualLiveShopItemGroup(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    paid_virtual_live_shop_item_ids: Optional[List[int]] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class PaidVirtualLive(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    virtual_live_part: Optional[int] = None
    paid_virtual_live_type: Optional[Union[PaidVirtualLiveType, Unknown]] = None
    units: Optional[List[Union[Unit, Unknown]]] = None
    icon_asset_bundle_name: Optional[str] = None
    background_asset_bundle_name: Optional[str] = None


class VirtualLiveCheerMessage(Model):
    id: Optional[int] = None
    virtual_live_type: Optional[Union[VirtualLiveType, Unknown]] = None
    resource_type: Optional[Union[ResourceType, Unknown]] = None
    from_cost_virtual_coin: Optional[int] = None
    to_cost_virtual_coin: Optional[int] = None
    from_cost: Optional[int] = None
    to_cost: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    message_length_limit: Optional[int] = None
    display_sec: Optional[float] = None
    message_size: Optional[Union[MessageSize, Unknown]] = None
    color_code: Optional[str] = None
    virtual_live_cheer_message_display_limit_id: Optional[int] = None


class VirtualLiveCheerMessageDisplayLimit(Model):
    id: Optional[int] = None
    display_limit: Optional[int] = None


class VirtualLiveTicket(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    virtual_live_ticket_type: Optional[Union[VirtualLiveTicketType, Unknown]] = None
    name: Optional[str] = None
    flavor_text: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class VirtualLivePamphlet(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    name: Optional[str] = None
    flavor_text: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class AvatarAccessory(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    part: Optional[Union[AccessoryPart, Unknown]] = None
    asset_bundle_name: Optional[str] = None


class AvatarCostume(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class AvatarMotion(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    sync_music_flg: Optional[bool] = None
    repeat_count: Optional[int] = None
    asset_bundle_name: Optional[str] = None


class AvatarSkinColor(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    color_code: Optional[str] = None


class AvatarCoordinate(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    skin_color_code: Optional[str] = None
    costume_asset_bundle_name: Optional[str] = None
    accessory_part: Optional[Union[AccessoryPart, Unknown]] = None
    accessory_asset_bundle_name: Optional[str] = None


class NgWord(Model):
    id: Optional[int] = None
    word: Optional[str] = None


class RuleSlide(Model):
    id: Optional[int] = None
    rule_slide_type: Optional[Union[RuleSlideType, Unknown]] = None
    asset_bundle_name: Optional[str] = None


class Facility(Model):
    id: Optional[int] = None
    facility_type: Optional[Union[FacilityType, Unknown]] = None
    release_condition_id: Optional[int] = None
    and_release_condition_id: Optional[int] = None


class OneTimeBehavior(Model):
    id: Optional[int] = None
    one_time_behavior_type: Optional[Union[OneTimeBehaviorType, Unknown]] = None
    release_condition_id: Optional[int] = None


class LoginBonus(Model):
    id: Optional[int] = None
    day: Optional[int] = None
    resource_box_id: Optional[int] = None


class BeginnerLoginBonus(Model):
    id: Optional[int] = None
    day: Optional[int] = None
    resource_box_id: Optional[int] = None
    login_bonus_id: Optional[int] = None


class BeginnerLoginBonusSummary(Model):
    id: Optional[int] = None
    login_bonus_id: Optional[int] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None


class LimitedLoginBonusDetail(Model):
    id: Optional[int] = None
    limited_login_bonus_id: Optional[int] = None
    day: Optional[int] = None
    resource_box_id: Optional[int] = None


class LimitedLoginBonus(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    asset_bundle_name: Optional[str] = None
    close_at: Optional[datetime] = None
    limited_login_bonus_details: Optional[List[LimitedLoginBonusDetail]] = None


class LoginBonusLive2d(Live2d):
    serif: Optional[str] = None
    voice: Optional[str] = None
    published_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None


class EventRankingReward(Model):
    id: Optional[int] = None
    event_ranking_reward_range_id: Optional[int] = None
    resource_box_id: Optional[int] = None


class EventRankingRewardRange(Model):
    id: Optional[int] = None
    event_id: Optional[int] = None
    from_rank: Optional[int] = None
    to_rank: Optional[int] = None
    event_ranking_rewards: Optional[List[EventRankingReward]] = None
    is_to_rank_border: Optional[bool] = None


class Event(Model):
    id: Optional[int] = None
    event_type: Optional[Union[EventType, Unknown]] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    bgm_asset_bundle_name: Optional[str] = None
    start_at: Optional[datetime] = None
    aggregate_at: Optional[datetime] = None
    ranking_announce_at: Optional[datetime] = None
    distribution_start_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    distribution_end_at: Optional[datetime] = None
    virtual_live_id: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None
    event_ranking_reward_ranges: Optional[List[EventRankingRewardRange]] = None
    event_point_asset_bundle_name: Optional[str] = None
    event_only_component_display_start_at: Optional[datetime] = None
    event_only_component_display_end_at: Optional[datetime] = None


class EventMusic(Model):
    event_id: Optional[int] = None
    music_id: Optional[int] = None
    seq: Optional[int] = None
    release_condition_id: Optional[int] = None


class EventDeckBonus(Model):
    id: Optional[int] = None
    event_id: Optional[int] = None
    game_character_unit_id: Optional[int] = None
    card_attr: Optional[Union[CardAttr, Unknown]] = None
    bonus_rate: Optional[float] = None


class EventRarityBonusRate(Model):
    id: Optional[int] = None
    card_rarity_type: Optional[Union[CardRarityType, Unknown]] = None
    master_rank: Optional[int] = None
    bonus_rate: Optional[float] = None


class EventItem(Model):
    id: Optional[int] = None
    event_id: Optional[int] = None
    name: Optional[str] = None
    flavor_text: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    game_character_id: Optional[int] = None


class EpisodeReward(Model):
    story_type: Optional[Union[StoryType, Unknown]] = None
    resource_box_id: Optional[int] = None


class EventStoryEpisode(Model):
    id: Optional[int] = None
    event_story_id: Optional[int] = None
    episode_no: Optional[int] = None
    title: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    scenario_id: Optional[str] = None
    release_condition_id: Optional[int] = None
    episode_rewards: Optional[List[EpisodeReward]] = None
    game_character_id: Optional[int] = None


class EventStory(Model):
    id: Optional[int] = None
    event_id: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    event_story_episodes: Optional[List[EventStoryEpisode]] = None
    banner_game_character_unit_id: Optional[int] = None
    outline: Optional[str] = None


class EventExchangeCost(Cost):
    id: Optional[int] = None
    event_exchange_id: Optional[int] = None


class EventExchange(Model):
    id: Optional[int] = None
    event_exchange_summary_id: Optional[int] = None
    seq: Optional[int] = None
    resource_box_id: Optional[int] = None
    exchange_limit: Optional[int] = None
    event_exchange_cost: Optional[EventExchangeCost] = None
    game_character_id: Optional[int] = None


class EventExchangeSummary(Model):
    id: Optional[int] = None
    event_id: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    event_exchanges: Optional[List[EventExchange]] = None


class EventStoryUnit(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    event_story_id: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None
    event_story_unit_relation: Optional[Union[EventStoryUnitRelation, Unknown]] = None


class EventCard(Model):
    id: Optional[int] = None
    card_id: Optional[int] = None
    event_id: Optional[int] = None
    bonus_rate: Optional[float] = None


class PreliminaryTournamentCard(Model):
    id: Optional[int] = None
    preliminary_tournament_id: Optional[int] = None
    card_id: Optional[int] = None


class PreliminaryTournamentMusic(Model):
    id: Optional[int] = None
    preliminary_tournament_id: Optional[int] = None
    music_difficulty_id: Optional[int] = None
    music_id: Optional[int] = None


class PreliminaryTournament(Model):
    id: Optional[int] = None
    preliminary_tournament_type: Optional[Union[PreliminaryTournamentType, Unknown]] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    release_condition_id: Optional[int] = None
    preliminary_tournament_cards: Optional[List[PreliminaryTournamentCard]] = None
    preliminary_tournament_musics: Optional[List[PreliminaryTournamentMusic]] = None


class CheerfulCarnivalSummary(Model):
    id: Optional[int] = None
    event_id: Optional[int] = None
    theme: Optional[str] = None
    midterm_announce1_at: Optional[datetime] = None
    midterm_announce2_at: Optional[datetime] = None
    asset_bundle_name: Optional[str] = None


class CheerfulCarnivalTeam(Model):
    id: Optional[int] = None
    event_id: Optional[int] = None
    seq: Optional[int] = None
    team_name: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class CheerfulCarnivalPartyName(Model):
    id: Optional[int] = None
    party_name: Optional[str] = None
    game_character_unit_id1: Optional[int] = None
    game_character_unit_id2: Optional[int] = None
    game_character_unit_id3: Optional[int] = None
    game_character_unit_id4: Optional[int] = None
    game_character_unit_id5: Optional[int] = None


class CheerfulCarnivalCharacterPartyName(Model):
    id: Optional[int] = None
    character_party_name: Optional[str] = None
    game_character_unit_id: Optional[int] = None


class CheerfulCarnivalLiveTeamPointBonus(Model):
    id: Optional[int] = None
    team_point_bonus_rate: Optional[int] = None


class CheerfulCarnivalReward(Model):
    id: Optional[int] = None
    event_id: Optional[int] = None
    cheerful_carnival_team_id: Optional[int] = None
    resource_box_id: Optional[int] = None


class CheerfulCarnivalResultReward(Model):
    id: Optional[int] = None
    event_id: Optional[int] = None
    cheerful_carnival_team_point_term_type: Optional[
        Union[CheerfulCarnivalTeamPointTermType, Unknown]] = None
    cheerful_carnival_result_type: Optional[Union[CheerfulCarnivalResultType, Unknown]] = None
    resource_box_id: Optional[int] = None


class Appeal(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    appeal_target_type: Optional[Union[AppealTargetType, Unknown]] = None
    appeal_type: Optional[Union[AppealType, Unknown]] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    appeal_read_condition_type: Optional[Union[AppealReadConditionType, Unknown]] = None
    text: Optional[str] = None


class Boost(Model):
    id: Optional[int] = None
    cost_boost: Optional[int] = None
    is_event_only: Optional[bool] = None
    exp_rate: Optional[int] = None
    reward_rate: Optional[int] = None
    live_point_rate: Optional[int] = None
    event_point_rate: Optional[int] = None
    bonds_exp_rate: Optional[int] = None


class BoostPresent(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    recovery_value: Optional[int] = None
    present_limit: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    is_unlimited_receive: Optional[bool] = None
    boost_present_cost_id: Optional[int] = None


class BoostPresentCost(Cost):
    id: Optional[int] = None


class EpisodeCharacter(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    character2d_id: Optional[int] = None
    story_type: Optional[Union[StoryType, Unknown]] = None
    episode_id: Optional[int] = None


class CustomProfileTextColor(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    color_code: Optional[str] = None


class CustomProfileTextFont(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    font_name: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class CustomProfileResource(Model):
    custom_profile_resource_type: Optional[Union[CustomProfileResourceType, Unknown]] = None
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    resource_load_type: Optional[Union[ResourceLoadType, Unknown]] = None
    resource_load_val: Optional[str] = None
    file_name: Optional[str] = None
    group_id: Optional[int] = None


class CustomProfilePlayerInfoResource(CustomProfileResource):
    pass


class CustomProfileGeneralBackgroundResource(CustomProfileResource):
    pass


class CustomProfileStoryBackgroundResource(CustomProfileResource):
    pass


class CustomProfileCollectionResource(CustomProfileResource):
    custom_profile_resource_collection_type: Optional[
        Union[CustomProfileResourceCollectionType, Unknown]] = None


class CustomProfileMemberStandingPictureResource(CustomProfileResource):
    character_id: Optional[int] = None


class CustomProfileShapeResource(CustomProfileResource):
    pass


class CustomProfileEtcResource(CustomProfileResource):
    pass


class CustomProfileGachaBehavior(Model):
    id: Optional[int] = None
    custom_profile_gacha_id: Optional[int] = None
    seq: Optional[int] = None
    cost_resource_type: Optional[Union[ResourceType, Unknown]] = None
    cost_resource_quantity: Optional[int] = None
    spin_count: Optional[int] = None


class CustomProfileGachaDetail(Model):
    id: Optional[int] = None
    custom_profile_gacha_id: Optional[int] = None
    custom_profile_resource_type: Optional[Union[CustomProfileResourceType, Unknown]] = None
    custom_profile_resource_id: Optional[int] = None
    custom_profile_resource_quantity: Optional[int] = None
    weight: Optional[int] = None


class CustomProfileGacha(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    asset_bundle_name: Optional[str] = None
    description: Optional[str] = None
    notice: Optional[str] = None
    custom_profile_gacha_behaviors: Optional[List[CustomProfileGachaBehavior]] = None
    custom_profile_gacha_details: Optional[List[CustomProfileGachaDetail]] = None


class CustomProfileGachaTab(Model):
    id: Optional[int] = None
    child_custom_profile_gacha_ids: Optional[List[int]] = None
    seq: Optional[int] = None
    asset_bundle_name: Optional[str] = None


class StreamingLiveBgm(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    seq: Optional[int] = None
    music_vocal_id: Optional[int] = None


class StreamingLiveSetlist(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    chapter_id: Optional[int] = None
    name: Optional[str] = None
    character_ids: Optional[List[int]] = None
    music_id: Optional[int] = None


class StreamingLiveArchive(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    virtual_live_part: Optional[int] = None
    streaming_live_category_id: Optional[int] = None
    streaming_live_setlists: Optional[List[StreamingLiveSetlist]] = None
    play_time: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class StreamingLiveCategoryItem(Model):
    id: Optional[int] = None
    name: Optional[str] = None


class Omikuji(Model):
    id: Optional[int] = None
    omikuji_group_id: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None
    fortune_type: Optional[Union[FortuneType, Unknown]] = None
    summary: Optional[str] = None
    title1: Optional[str] = None
    description1: Optional[str] = None
    title2: Optional[str] = None
    description2: Optional[str] = None
    title3: Optional[str] = None
    description3: Optional[str] = None
    unit_asset_bundle_name: Optional[str] = None
    fortune_asset_bundle_name: Optional[str] = None
    omikuji_cover_asset_bundle_name: Optional[str] = None
    unit_file_path: Optional[str] = None
    fortune_file_path: Optional[str] = None
    omikuji_cover_file_path: Optional[str] = None


class OmikujiGroup(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    appeal_asset_bundle_name: Optional[str] = None
    sound_asset_bundle_name: Optional[str] = None


class OmikujiRate(Model):
    id: Optional[int] = None
    omikuji_group_id: Optional[int] = None
    fortune_type: Optional[Union[FortuneType, Unknown]] = None
    rate: Optional[float] = None


class OmikujiCost(Cost):
    id: Optional[int] = None
    omikuji_group_id: Optional[int] = None
    seq: Optional[int] = None


class OmikujiReward(Model):
    id: Optional[int] = None
    omikuji_group_id: Optional[int] = None
    seq: Optional[int] = None
    resource_type: Optional[Union[ResourceType, Unknown]] = None
    resource_id: Optional[int] = None
    resource_quantity: Optional[int] = None


class VirtualBoothShop(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    virtual_booth_shop_type: Optional[Union[VirtualBoothShopType, Unknown]] = None
    target_id: Optional[int] = None


class SpecialSeason(Model):
    id: Optional[int] = None
    special_season_type: Optional[Union[SpecialSeasonType, Unknown]] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    priority: Optional[int] = None


class SpecialSeasonArea(Model):
    id: Optional[int] = None
    special_season_id: Optional[int] = None
    area_id: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    file_name: Optional[str] = None
    special_season_area_use_type: Optional[Union[SpecialSeasonAreaUseType, Unknown]] = None


class RankMatchPenalty(Model):
    id: Optional[int] = None
    count: Optional[int] = None
    rank_match_penalty_type: Optional[Union[RankMatchPenaltyType, Unknown]] = None
    rank_match_penalty_type_value: Optional[int] = None


class RankMatchPlacement(Model):
    id: Optional[int] = None
    rank_match_placement_condition_type: Optional[str] = None
    tier_behavior_type: Optional[Union[TierBehaviorType, Unknown]] = None
    tier_behavior_type_value: Optional[int] = None
    rank_match_placement_condition_type_value: Optional[int] = None


class RankMatchBonusPointCondition(Model):
    id: Optional[int] = None
    rank_match_bonus_point_condition_type: Optional[Union[RankMatchBonusPointConditionType, Unknown]] = None
    group_id: Optional[int] = None
    priority: Optional[int] = None
    calc_type: Optional[Union[CalcType, Unknown]] = None
    bonus_point: Optional[int] = None


class RankMatchSeasonPlayableTime(Model):
    id: Optional[int] = None
    rank_match_season_id: Optional[int] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None


class RankMatchSeasonTierMusicPlayLevel(Model):
    id: Optional[int] = None
    rank_match_season_id: Optional[int] = None
    rank_match_tier_id: Optional[int] = None
    from_play_level: Optional[int] = None
    to_play_level: Optional[int] = None
    from_play_level_for_append: Optional[int] = None
    to_play_level_for_append: Optional[int] = None


class RankMatchSeasonTierReward(Model):
    id: Optional[int] = None
    rank_match_season_id: Optional[int] = None
    rank_match_tier_id: Optional[int] = None
    resource_box_id: Optional[int] = None


class RankMatchSeason(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    start_at: Optional[datetime] = None
    aggregated_at: Optional[datetime] = None
    ranking_published_at: Optional[datetime] = None
    batch_execution_at: Optional[datetime] = None
    distribution_start_at: Optional[datetime] = None
    distribution_end_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    asset_bundle_name: Optional[str] = None
    is_display_result: Optional[bool] = None
    rank_match_season_playable_times: Optional[
        List[RankMatchSeasonPlayableTime]
    ] = None
    rank_match_season_tier_music_play_levels: Optional[
        List[RankMatchSeasonTierMusicPlayLevel]
    ] = None
    rank_match_season_tier_rewards: Optional[List[RankMatchSeasonTierReward]] = None


class RankMatchTier(Model):
    id: Optional[int] = None
    rank_match_grade_id: Optional[int] = None
    rank_match_class_id: Optional[int] = None
    tier: Optional[int] = None
    total_music_difficulty: Optional[int] = None
    point: Optional[int] = None
    grade_asset_bundle_name: Optional[str] = None
    tier_asset_bundle_name: Optional[str] = None


class RankMatchTierBonusPoint(Model):
    id: Optional[int] = None
    rank_match_tier_id: Optional[int] = None
    max_bonus_point: Optional[int] = None
    reward_point: Optional[int] = None


class RankMatchGrade(Model):
    id: Optional[int] = None
    name: Optional[str] = None


class RankMatchClass(Model):
    id: Optional[int] = None
    name: Optional[str] = None


class LimitedTitleScreen(Model):
    id: Optional[int] = None
    priority: Optional[int] = None
    download_start_at: Optional[datetime] = None
    download_end_at: Optional[datetime] = None
    display_start_at: Optional[datetime] = None
    display_end_at: Optional[datetime] = None
    bg_asset_bundle_name: Optional[str] = None
    logo_asset_bundle_name: Optional[str] = None
    bgm_asset_bundle_name: Optional[str] = None
    start_effect_asset_bundle_name: Optional[str] = None


class PanelMission(Model):
    id: Optional[int] = None
    panel_mission_sheet_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    seq: Optional[int] = None
    panel_mission_type: Optional[Union[PanelMissionType, Unknown]] = None
    requirement1: Optional[int] = None
    rewards: Optional[List[MissionReward]] = None
    requirement2: Optional[int] = None


class MissionSheetReward(MissionReward):
    worksheet_version: Optional[str] = None


class PanelMissionSheet(Model):
    id: Optional[int] = None
    panel_mission_sheet_group_id: Optional[int] = None
    name: Optional[str] = None
    seq: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    panel_missions: Optional[List[PanelMission]] = None
    rewards: Optional[List[MissionSheetReward]] = None


class PanelMissionSheetGroup(Model):
    id: Optional[int] = None
    panel_mission_campaign_id: Optional[int] = None
    name: Optional[str] = None
    selectable_limit: Optional[int] = None
    seq: Optional[int] = None
    panel_mission_sheets: Optional[List[PanelMissionSheet]] = None


class PanelMissionCampaign(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    bgm_asset_bundle_name: Optional[str] = None
    selectable_limit: Optional[int] = None
    start_at: Optional[datetime] = None
    progress_end_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    information_id: Optional[int] = None
    panel_mission_sheet_groups: Optional[List[PanelMissionSheetGroup]] = None


class EventMission(Model):
    id: Optional[int] = None
    event_id: Optional[int] = None
    seq: Optional[int] = None
    event_mission_type: Optional[Union[EventMissionType, Unknown]] = None
    event_mission_category: Optional[Union[EventMissionCategory, Unknown]] = None
    requirement1: Optional[int] = None
    sentence: Optional[str] = None
    rewards: Optional[List[MissionReward]] = None
    requirement2: Optional[int] = None


class BackgroundMusic(Model):
    id: Optional[int] = None
    title: Optional[str] = None


class OfflineEvent(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    url: Optional[str] = None
    display_start_at: Optional[datetime] = None
    entry_evaluation_start_at: Optional[datetime] = None
    entry_start_at: Optional[datetime] = None
    entry_end_at: Optional[datetime] = None
    condition_continuous_buy_high_tier_count: Optional[int] = None


class Another3dmvCutIn(Model):
    id: Optional[int] = None
    card_id: Optional[int] = None
    music_id: Optional[int] = None
    cut_in_no: Optional[int] = None


class LimitedTimeMusic(Model):
    id: Optional[int] = None
    music_id: Optional[int] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None


class MusicArtist(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    pronunciation: Optional[str] = None


class BeginnerMissionV2(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    beginner_mission_v2_type: Optional[Union[BeginnerMissionType, Unknown]] = None
    beginner_mission_v2_category: Optional[Union[BeginnerMissionCategory, Unknown]] = None
    condition_value: Optional[int] = None
    requirement: Optional[int] = None
    sentence: Optional[str] = None
    rewards: Optional[List[MissionReward]] = None


class CharacterMissionV2ExJson(Model):
    id: Optional[int] = None
    character_mission_type: Optional[Union[CharacterMissionType, Unknown]] = None
    character_mission_ex_type: Optional[Union[CharacterMissionType, Unknown]] = None
    resource_type: Optional[Union[ResourceType, Unknown]] = None


class FriendInvitationCampaignMissionReward(Model):
    id: Optional[int] = None
    count_group_id: Optional[int] = None
    count: Optional[int] = None
    resource_box_id: Optional[int] = None


class FriendInvitationCampaignMission(Model):
    id: Optional[int] = None
    mission_type: Optional[Union[FriendInvitationCampaignMissionType, Unknown]] = None
    mission_category_id: Optional[int] = None
    name: Optional[str] = None
    requirement: Optional[int] = None
    reward: Optional[List[FriendInvitationCampaignMissionReward]] = None


class FriendInvitationCampaign(Model):
    id: Optional[int] = None
    group_id: Optional[int] = None
    title: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    start_at: Optional[datetime] = None
    progress_end_at: Optional[datetime] = None
    receive_reward_end_at: Optional[int] = None
    closed_at: Optional[int] = None
    missions: Optional[List[FriendInvitationCampaignMission]] = None


class UnitStoryEpisodeGroup(Model):
    id: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None
    unit_episode_category: Optional[Union[Unit, Unknown]] = None
    outline: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class EpisodeBackgroundMusic(Model):
    id: Optional[int] = None
    story_type: Optional[Union[StoryType, Unknown]] = None
    episode_id: Optional[int] = None
    background_music_id: Optional[int] = None


class VirtualItemRelation(Model):
    id: Optional[int] = None
    group_id: Optional[int] = None
    virtual_item_id: Optional[int] = None


class VirtualLiveCheerMessageRelation(Model):
    id: Optional[int] = None
    group_id: Optional[int] = None
    virtual_live_cheer_message_id: Optional[int] = None


class WorldBloom(Model):
    id: Optional[int] = None
    event_id: Optional[int] = None
    game_character_id: Optional[int] = None
    chapter_no: Optional[int] = None
    chapter_start_at: Optional[int] = None
    aggregate_at: Optional[int] = None
    chapter_end_at: Optional[int] = None
    costume2d_id: Optional[int] = None
    is_supplemental: Optional[bool] = None


class WorldBloomDifferentAttributeBonus(Model):
    attribute_count: Optional[int] = None
    bonus_rate: Optional[float] = None


class WorldBloomSupportDeckCharacterBonus(Model):
    id: Optional[int] = None
    world_bloom_support_deck_character_type: Optional[
        Union[WorldBloomSupportDeckCharacterType, Unknown]] = None
    bonus_rate: Optional[float] = None


class WorldBloomSupportDeckMasterRankBonus(Model):
    id: Optional[int] = None
    master_rank: Optional[int] = None
    bonus_rate: Optional[float] = None


class WorldBloomSupportDeckSkillLevelBonus(Model):
    id: Optional[int] = None
    skill_level: Optional[int] = None
    bonus_rate: Optional[float] = None


class WorldBloomSupportDeckBonus(Model):
    card_rarity_type: Optional[Union[CardRarityType, Unknown]] = None
    world_bloom_support_deck_character_bonuses: Optional[
        List[WorldBloomSupportDeckCharacterBonus]] = None
    world_bloom_support_deck_master_rank_bonuses: Optional[
        List[WorldBloomSupportDeckMasterRankBonus]] = None
    world_bloom_support_deck_skill_level_bonuses: Optional[
        List[WorldBloomSupportDeckSkillLevelBonus]] = None


class WorldBloomChapterRankingRewardRange(Model):
    id: Optional[int] = None
    event_id: Optional[int] = None
    game_character_id: Optional[int] = None
    from_rank: Optional[int] = None
    to_rank: Optional[int] = None
    is_to_rank_border: Optional[bool] = None
    resource_box_id: Optional[int] = None


class CardExtra(Model):
    id: Optional[int] = None
    card_id: Optional[int] = None
    resource_box_id: Optional[int] = None


class SubGameCharacter(OutsideCharacter):
    pass


class CharacterArchiveVoice(Model):
    id: Optional[int] = None
    group_id: Optional[int] = None
    game_character_id: Optional[int] = None
    unit: Optional[Union[Unit, Unknown]] = None
    character_archive_voice_type: Optional[Union[CharacterArchiveVoiceType, Unknown]] = None
    display_phrase: Optional[str] = None
    display_phrase2: Optional[str] = None
    character_archive_voice_tag_id: Optional[int] = None
    asset_name: Optional[str] = None
    external_id: Optional[int] = None
    is_next_grade: Optional[bool] = None
    display_start_at: Optional[int] = None


class CharacterArchiveVoiceTag(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    character_archive_voice_tag_type: Optional[Union[CharacterArchiveVoiceTagType, Unknown]] = None
    name: Optional[str] = None


class LiveClearVoice(Model):
    id: Optional[int] = None
    game_character_unit_id: Optional[int] = None
    is_next_grade: Optional[bool] = None
    live_clear_voice_type: Optional[Union[LiveClearVoiceType, Unknown]] = None
    voice_file_name: Optional[str] = None


class AdReward(Model):
    id: Optional[int] = None
    ad_reward_play_type: Optional[Union[AdRewardPlayType, Unknown]] = None
    resource_box_id: Optional[int] = None
    live_bonus_count: Optional[int] = None
    daily_limit_count: Optional[int] = None
    display_flg: Optional[bool] = None
    start_at: Optional[int] = None
    end_at: Optional[int] = None


class MasterData(Model):
    game_characters: Optional[List[GameCharacter]] = None
    game_character_units: Optional[List[GameCharacterUnit]] = None
    outside_characters: Optional[List[OutsideCharacter]] = None
    character3ds: Optional[List[Character3d]] = None
    character2ds: Optional[List[Character2d]] = None
    character_profiles: Optional[List[CharacterProfile]] = None
    bonds: Optional[List[Bond]] = None
    bonds_live2ds: Optional[List[BondsLive2d]] = None
    bonds_rank_up_live2ds: Optional[List[BondsRankUpLive2d]] = None
    unit_profiles: Optional[List[UnitProfile]] = None
    action_sets: Optional[List[ActionSet]] = None
    areas: Optional[List[Area]] = None
    area_playlists: Optional[List[AreaPlaylist]] = None
    mob_characters: Optional[List[MobCharacter]] = None
    character_costumes: Optional[List[CharacterCostume]] = None
    card_costume3ds: Optional[List[CardCostume3d]] = None
    cards: Optional[List[Card]] = None
    skills: Optional[List[Skill]] = None
    card_episodes: Optional[List[CardEpisode]] = None
    card_rarities: Optional[List[CardRarity]] = None
    card_skill_costs: Optional[List[CardSkillCost]] = None
    musics: Optional[List[Music]] = None
    music_tags: Optional[List[MusicTag]] = None
    music_difficulties: Optional[List[MusicDifficulty]] = None
    music_vocals: Optional[List[MusicVocal]] = None
    music_dance_members: Optional[List[MusicDanceMember]] = None
    music_achievements: Optional[List[MusicAchievement]] = None
    music_video_characters: Optional[List[MusicVideoCharacter]] = None
    music_asset_variants: Optional[List[MusicAssetVariant]] = None
    music_collaborations: Optional[List[MusicCollaboration]] = None
    episode_music_video_costumes: Optional[List[EpisodeMusicVideoCostume]] = None
    music_originals: Optional[List[MusicOriginal]] = None
    release_conditions: Optional[List[ReleaseCondition]] = None
    play_level_scores: Optional[List[PlayLevelScore]] = None
    ingame_combos: Optional[List[IngameCombo]] = None
    ingame_notes: Optional[List[IngameNote]] = None
    ingame_note_judges: Optional[List[IngameNoteJudge]] = None
    ingame_play_levels: Optional[List[IngamePlayLevel]] = None
    ingame_cutins: Optional[List[IngameCutin]] = None
    ingame_cutin_characters: Optional[List[IngameCutinCharacter]] = None
    ingame_judge_frames: Optional[List[IngameJudgeFrame]] = None
    ingame_note_judge_technical_scores: Optional[
        List[IngameNoteJudgeTechnicalScore]
    ] = None
    shops: Optional[List[Shop]] = None
    shop_items: Optional[List[ShopItem]] = None
    costume3d_shop_items: Optional[List[Costume3dShopItem]] = None
    area_items: Optional[List[AreaItem]] = None
    area_item_levels: Optional[List[AreaItemLevel]] = None
    materials: Optional[List[Material]] = None
    gachas: Optional[List[Gacha]] = None
    gacha_bonuses: Optional[List[GachaBonus]] = None
    gacha_bonus_points: Optional[List[GachaBonusPoint]] = None
    gacha_extras: Optional[List[GachaExtra]] = None
    gift_gacha_exchanges: Optional[List[GiftGachaExchange]] = None
    gacha_tabs: Optional[List[GachaTab]] = None
    practice_tickets: Optional[List[PracticeTicket]] = None
    skill_practice_tickets: Optional[List[SkillPracticeTicket]] = None
    levels: Optional[List[Level]] = None
    unit_stories: Optional[List[UnitStory]] = None
    special_stories: Optional[List[SpecialStory]] = None
    configs: Optional[List[Config]] = None
    client_configs: Optional[List[ClientConfig]] = None
    wordings: Optional[List[Wording]] = None
    costume3ds: Optional[List[Costume3d]] = None
    costume3d_models: Optional[List[Costume3dModel]] = None
    costume3d_model_available_patterns: Optional[
        List[Costume3dModelAvailablePattern]
    ] = None
    game_character_unit3d_motions: Optional[List[GameCharacterUnit3dMotion]] = None
    costume2ds: Optional[List[Costume2d]] = None
    costume2d_groups: Optional[List[Costume2dGroup]] = None
    topics: Optional[List[Topic]] = None
    live_stages: Optional[List[LiveStage]] = None
    stamps: Optional[List[Stamp]] = None
    multi_live_lobbies: Optional[List[MultiLiveLobby]] = None
    master_lessons: Optional[List[MasterLesson]] = None
    master_lesson_rewards: Optional[List[MasterLessonReward]] = None
    card_exchange_resources: Optional[List[CardExchangeResource]] = None
    material_exchanges: Optional[List[MaterialExchange]] = None
    material_exchange_summaries: Optional[List[MaterialExchangeSummary]] = None
    boost_items: Optional[List[BoostItem]] = None
    billing_products: Optional[List[BillingProduct]] = None
    billing_shop_items: Optional[List[BillingShopItem]] = None
    billing_shop_item_exchange_costs: Optional[
        List[BillingShopItemExchangeCost]
    ] = None
    billing_shop_item_groups: Optional[List[BillingShopItemGroup]] = None
    colorful_passes: Optional[List[ColorfulPass]] = None
    colorful_pass_v2s: Optional[List[ColorfulPassV2]] = None
    jewel_behaviors: Optional[List[JewelBehavior]] = None
    character_ranks: Optional[List[CharacterRank]] = None
    character_mission_v2s: Optional[List[CharacterMissionV2]] = None
    character_mission_v2_parameter_groups: Optional[
        List[CharacterMissionV2ParameterGroup]
    ] = None
    character_mission_v2_area_items: Optional[List[CharacterMissionV2AreaItem]] = None
    system_live2ds: Optional[List[SystemLive2d]] = None
    normal_missions: Optional[List[NormalMission]] = None
    beginner_missions: Optional[List[BeginnerMission]] = None
    resource_boxes: Optional[List[ResourceBox]] = None
    live_mission_periods: Optional[List[LiveMissionPeriod]] = None
    live_missions: Optional[List[LiveMission]] = None
    live_mission_passes: Optional[List[LiveMissionPass]] = None
    penlight_colors: Optional[List[PenlightColor]] = None
    penlights: Optional[List[Penlight]] = None
    live_talks: Optional[List[LiveTalk]] = None
    tips: Optional[List[Tip]] = None
    gacha_ceil_items: Optional[List[GachaCeilItem]] = None
    gacha_ceil_exchange_summaries: Optional[List[GachaCeilExchangeSummary]] = None
    player_rank_rewards: Optional[List[PlayerRankReward]] = None
    gacha_tickets: Optional[List[GachaTicket]] = None
    honor_groups: Optional[List[HonorGroup]] = None
    honors: Optional[List[Honor]] = None
    honor_missions: Optional[List[HonorMission]] = None
    bonds_honors: Optional[List[BondsHonor]] = None
    bonds_honor_words: Optional[List[BondsHonorWord]] = None
    bonds_rewards: Optional[List[BondsReward]] = None
    challenge_lives: Optional[List[ChallengeLive]] = None
    challenge_live_decks: Optional[List[ChallengeLiveDeck]] = None
    challenge_live_stages: Optional[List[ChallengeLiveStage]] = None
    challenge_live_stage_exs: Optional[List[ChallengeLiveStageEx]] = None
    challenge_live_high_score_rewards: Optional[
        List[ChallengeLiveHighScoreReward]
    ] = None
    challenge_live_characters: Optional[List[ChallengeLiveCharacter]] = None
    challenge_live_play_day_reward_periods: Optional[
        List[ChallengeLivePlayDayRewardPeriod]
    ] = None
    virtual_lives: Optional[List[VirtualLive]] = None
    virtual_shops: Optional[List[VirtualShop]] = None
    paid_virtual_live_shop_items: Optional[List[PaidVirtualLiveShopItem]] = None
    paid_virtual_live_shop_item_groups: Optional[
        List[PaidVirtualLiveShopItemGroup]
    ] = None
    paid_virtual_lives: Optional[List[PaidVirtualLive]] = None
    virtual_items: Optional[List[VirtualItem]] = None
    virtual_live_cheer_messages: Optional[List[VirtualLiveCheerMessage]] = None
    virtual_live_cheer_message_display_limits: Optional[
        List[VirtualLiveCheerMessageDisplayLimit]
    ] = None
    virtual_live_tickets: Optional[List[VirtualLiveTicket]] = None
    virtual_live_pamphlets: Optional[List[VirtualLivePamphlet]] = None
    avatar_accessories: Optional[List[AvatarAccessory]] = None
    avatar_costumes: Optional[List[AvatarCostume]] = None
    avatar_motions: Optional[List[AvatarMotion]] = None
    avatar_skin_colors: Optional[List[AvatarSkinColor]] = None
    avatar_coordinates: Optional[List[AvatarCoordinate]] = None
    ng_words: Optional[List[NgWord]] = None
    rule_slides: Optional[List[RuleSlide]] = None
    facilities: Optional[List[Facility]] = None
    one_time_behaviors: Optional[List[OneTimeBehavior]] = None
    login_bonuses: Optional[List[LoginBonus]] = None
    beginner_login_bonuses: Optional[List[BeginnerLoginBonus]] = None
    beginner_login_bonus_summaries: Optional[List[BeginnerLoginBonusSummary]] = None
    limited_login_bonuses: Optional[List[LimitedLoginBonus]] = None
    login_bonus_live2ds: Optional[List[LoginBonusLive2d]] = None
    events: Optional[List[Event]] = None
    event_musics: Optional[List[EventMusic]] = None
    event_deck_bonuses: Optional[List[EventDeckBonus]] = None
    event_rarity_bonus_rates: Optional[List[EventRarityBonusRate]] = None
    event_items: Optional[List[EventItem]] = None
    event_stories: Optional[List[EventStory]] = None
    event_exchange_summaries: Optional[List[EventExchangeSummary]] = None
    event_story_units: Optional[List[EventStoryUnit]] = None
    event_cards: Optional[List[EventCard]] = None
    preliminary_tournaments: Optional[List[PreliminaryTournament]] = None
    cheerful_carnival_summaries: Optional[List[CheerfulCarnivalSummary]] = None
    cheerful_carnival_teams: Optional[List[CheerfulCarnivalTeam]] = None
    cheerful_carnival_party_names: Optional[List[CheerfulCarnivalPartyName]] = None
    cheerful_carnival_character_party_names: Optional[
        List[CheerfulCarnivalCharacterPartyName]
    ] = None
    cheerful_carnival_live_team_point_bonuses: Optional[
        List[CheerfulCarnivalLiveTeamPointBonus]
    ] = None
    cheerful_carnival_rewards: Optional[List[CheerfulCarnivalReward]] = None
    cheerful_carnival_result_rewards: Optional[
        List[CheerfulCarnivalResultReward]
    ] = None
    appeals: Optional[List[Appeal]] = None
    boosts: Optional[List[Boost]] = None
    boost_presents: Optional[List[BoostPresent]] = None
    boost_present_costs: Optional[List[BoostPresentCost]] = None
    episode_characters: Optional[List[EpisodeCharacter]] = None
    custom_profile_text_colors: Optional[List[CustomProfileTextColor]] = None
    custom_profile_text_fonts: Optional[List[CustomProfileTextFont]] = None
    custom_profile_player_info_resources: Optional[
        List[CustomProfilePlayerInfoResource]
    ] = None
    custom_profile_general_background_resources: Optional[
        List[CustomProfileGeneralBackgroundResource]
    ] = None
    custom_profile_story_background_resources: Optional[
        List[CustomProfileStoryBackgroundResource]
    ] = None
    custom_profile_collection_resources: Optional[
        List[CustomProfileCollectionResource]
    ] = None
    custom_profile_member_standing_picture_resources: Optional[
        List[CustomProfileMemberStandingPictureResource]
    ] = None
    custom_profile_shape_resources: Optional[List[CustomProfileShapeResource]] = None
    custom_profile_etc_resources: Optional[List[CustomProfileEtcResource]] = None
    custom_profile_member_resource_exclude_cards: Optional[List] = None
    custom_profile_gachas: Optional[List[CustomProfileGacha]] = None
    custom_profile_gacha_tabs: Optional[List[CustomProfileGachaTab]] = None
    streaming_live_bgms: Optional[List[StreamingLiveBgm]] = None
    streaming_live_archives: Optional[List[StreamingLiveArchive]] = None
    streaming_live_category: Optional[List[StreamingLiveCategoryItem]] = None
    omikujis: Optional[List[Omikuji]] = None
    omikuji_groups: Optional[List[OmikujiGroup]] = None
    omikuji_rates: Optional[List[OmikujiRate]] = None
    omikuji_costs: Optional[List[OmikujiCost]] = None
    omikuji_rewards: Optional[List[OmikujiReward]] = None
    virtual_booth_shops: Optional[List[VirtualBoothShop]] = None
    special_seasons: Optional[List[SpecialSeason]] = None
    special_season_areas: Optional[List[SpecialSeasonArea]] = None
    rank_match_penalties: Optional[List[RankMatchPenalty]] = None
    rank_match_placements: Optional[List[RankMatchPlacement]] = None
    rank_match_bonus_point_conditions: Optional[
        List[RankMatchBonusPointCondition]
    ] = None
    rank_match_seasons: Optional[List[RankMatchSeason]] = None
    rank_match_tiers: Optional[List[RankMatchTier]] = None
    rank_match_tier_bonus_points: Optional[List[RankMatchTierBonusPoint]] = None
    rank_match_grades: Optional[List[RankMatchGrade]] = None
    rank_match_classes: Optional[List[RankMatchClass]] = None
    limited_title_screens: Optional[List[LimitedTitleScreen]] = None
    panel_mission_campaigns: Optional[List[PanelMissionCampaign]] = None
    event_missions: Optional[List[EventMission]] = None
    background_musics: Optional[List[BackgroundMusic]] = None
    offline_events: Optional[List[OfflineEvent]] = None
    another_3dmv_cut_ins: Optional[List[Another3dmvCutIn]] = None
    limited_time_musics: Optional[List[LimitedTimeMusic]] = None
    music_artists: Optional[List[MusicArtist]] = None
    beginner_mission_v2s: Optional[List[BeginnerMissionV2]] = None

    character_mission_v2_ex_jsons: Optional[List[CharacterMissionV2ExJson]] = None
    friend_invitation_campaigns: Optional[List[FriendInvitationCampaign]] = None
    unit_story_episode_groups: Optional[List[UnitStoryEpisodeGroup]] = None
    episode_background_musics: Optional[List[EpisodeBackgroundMusic]] = None
    virtual_item_relations: Optional[List[VirtualItemRelation]] = None
    virtual_live_cheer_message_relations: Optional[List[VirtualLiveCheerMessageRelation]] = None
    world_blooms: Optional[List[WorldBloom]] = None
    world_bloom_different_attribute_bonuses: Optional[List[WorldBloomDifferentAttributeBonus]] = None
    world_bloom_support_deck_bonuses: Optional[List[WorldBloomSupportDeckBonus]] = None
    world_bloom_chapter_ranking_reward_ranges: Optional[
        List[WorldBloomChapterRankingRewardRange]] = None

    card_extras: Optional[List[CardExtra]] = None
    sub_game_characters: Optional[List[SubGameCharacter]] = None
    character_archive_voices: Optional[List[CharacterArchiveVoice]] = None
    character_archive_voice_tags: Optional[List[CharacterArchiveVoiceTag]] = None
    live_clear_voices: Optional[List[LiveClearVoice]] = None
    ad_rewards: Optional[List[AdReward]] = None
