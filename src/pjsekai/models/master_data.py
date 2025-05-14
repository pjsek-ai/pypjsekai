# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from typing import Optional
from pydantic import Field

from pjsekai.enums import *
from .model import Model, Empty


class GameCharacter(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    resource_id: Optional[int] = None
    first_name: Optional[str] = None
    given_name: Optional[str] = None
    first_name_ruby: Optional[str] = None
    given_name_ruby: Optional[str] = None
    gender: Optional[AllowUnknown[Gender]] = None
    height: Optional[float] = None
    live2d_height_adjustment: Optional[float] = None
    figure: Optional[AllowUnknown[Figure]] = None
    breast_size: Optional[AllowUnknown[BreastSize]] = None
    model_name: Optional[str] = None
    unit: Optional[AllowUnknown[Unit]] = None
    support_unit_type: Optional[AllowUnknown[SupportUnitType]] = None


class GameCharacterUnit(Model):
    id: Optional[int] = None
    game_character_id: Optional[int] = None
    unit: Optional[AllowUnknown[Unit]] = None
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
    character_type: Optional[AllowUnknown[CharacterType]] = None
    character_id: Optional[int] = None
    unit: Optional[AllowUnknown[Unit]] = None
    name: Optional[str] = None
    head_costume3d_id: Optional[int] = None
    hair_costume3d_id: Optional[int] = None
    body_costume3d_id: Optional[int] = None


class Character2d(Model):
    id: Optional[int] = None
    character_type: Optional[AllowUnknown[CharacterType]] = None
    character_id: Optional[int] = None
    unit: Optional[AllowUnknown[Unit]] = None
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
    unit: Optional[AllowUnknown[Unit]] = None
    asset_bundle_name: Optional[str] = None
    motion: Optional[str] = None
    expression: Optional[str] = None
    weight: Optional[int] = None


class BondsLive2d(Live2d):
    default_flg: Optional[bool] = None


class BondsRankUpLive2d(Live2d):
    default_flg: Optional[bool] = None


class UnitProfile(Model):
    unit: Optional[AllowUnknown[Unit]] = None
    unit_name: Optional[str] = None
    seq: Optional[int] = None
    profile_sentence: Optional[str] = None
    color_code: Optional[str] = None
    unit_profile_name: Optional[str] = None


class ActionSet(Model):
    id: Optional[int] = None
    area_id: Optional[int] = None
    script_id: Optional[str] = None
    character_ids: Optional[list[int]] = None
    archive_display_type: Optional[AllowUnknown[ArchiveDisplayType]] = None
    archive_published_at: Optional[datetime] = None
    release_condition_id: Optional[int] = None
    scenario_id: Optional[str] = None
    action_set_type: Optional[AllowUnknown[ActionSetType]] = None
    special_season_id: Optional[int] = None
    is_next_grade: Optional[bool] = None


class Area(Model):
    id: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    area_type: Optional[AllowUnknown[AreaType]] = None
    view_type: Optional[AllowUnknown[ViewType]] = None
    name: Optional[str] = None
    release_condition_id: Optional[int] = None
    label: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    is_base_area: Optional[bool] = None
    display_timeline_type: Optional[AllowUnknown[DisplayTimelineType]] = None
    group_id: Optional[int] = None
    sub_name: Optional[str] = None
    additional_area_type: Optional[AllowUnknown[AdditionalAreaType]] = None
    release_condition_id2: Optional[int] = None


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
    gender: Optional[AllowUnknown[Gender]] = None


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
    card_parameter_type: Optional[AllowUnknown[CardParameterType]] = None
    power: Optional[int] = None


class Cost(Model):
    resource_id: Optional[int] = None
    resource_type: Optional[AllowUnknown[ResourceType]] = None
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
    resources: Optional[list[Empty]] = None


class Card(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    character_id: Optional[int] = None
    card_rarity_type: Optional[AllowUnknown[CardRarityType]] = None
    special_training_power1_bonus_fixed: Optional[int] = None
    special_training_power2_bonus_fixed: Optional[int] = None
    special_training_power3_bonus_fixed: Optional[int] = None
    attr: Optional[AllowUnknown[CardAttr]] = None
    support_unit: Optional[AllowUnknown[Unit]] = None
    skill_id: Optional[int] = None
    card_skill_name: Optional[str] = None
    prefix: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    gacha_phrase: Optional[str] = None
    flavor_text: Optional[str] = None
    release_at: Optional[datetime] = None
    archive_published_at: Optional[datetime] = None
    card_parameters: Optional[list[CardParameter]] = None
    special_training_costs: Optional[list[SpecialTrainingCost]] = None
    master_lesson_achieve_resources: Optional[
        list[MasterLessonAchieveResource]
    ] = None
    archive_display_type: Optional[AllowUnknown[ArchiveDisplayType]] = None
    card_supply_id: Optional[int] = None
    special_training_skill_id: Optional[int] = None
    special_training_skill_name: Optional[str] = None


class SkillEffectDetail(Model):
    id: Optional[int] = None
    level: Optional[int] = None
    activate_effect_duration: Optional[float] = None
    activate_effect_value_type: Optional[AllowUnknown[ActivateEffectValueType]] = None
    activate_effect_value: Optional[int] = None
    activate_character_rank: Optional[int] = None
    activate_effect_value2: Optional[int] = None


class SkillEnhanceCondition(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    unit: Optional[AllowUnknown[Unit]] = None


class SkillEnhance(Model):
    id: Optional[int] = None
    skill_enhance_type: Optional[AllowUnknown[SkillEnhanceType]] = None
    activate_effect_value_type: Optional[AllowUnknown[ActivateEffectValueType]] = None
    activate_effect_value: Optional[int] = None
    skill_enhance_condition: Optional[SkillEnhanceCondition] = None


class SkillEffect(Model):
    id: Optional[int] = None
    skill_effect_type: Optional[AllowUnknown[SkillEffectType]] = None
    activate_notes_judgment_type: Optional[AllowUnknown[IngameNoteJudgeType]] = None
    skill_effect_details: Optional[list[SkillEffectDetail]] = None
    activate_life: Optional[int] = None
    condition_type: Optional[AllowUnknown[SkillEffectConditionType]] = None
    skill_enhance: Optional[SkillEnhance] = None
    activate_character_rank: Optional[int] = None
    activate_unit_count: Optional[int] = None


class Skill(Model):
    id: Optional[int] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    description_sprite_name: Optional[str] = None
    skill_filter_id: Optional[int] = None
    skill_effects: Optional[list[SkillEffect]] = None


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
    reward_resource_box_ids: Optional[list[int]] = None
    costs: Optional[list[Cost]] = None
    card_episode_part_type: Optional[AllowUnknown[CardEpisodePartType]] = None


class CardRarity(Model):
    card_rarity_type: Optional[AllowUnknown[CardRarityType]] = None
    seq: Optional[int] = None
    max_level: Optional[int] = None
    max_skill_level: Optional[int] = None
    training_max_level: Optional[int] = None


class CardSkillCost(Model):
    id: Optional[int] = None
    material_id: Optional[int] = None
    exp: Optional[int] = None
    character_id: Optional[int] = None
    unit: Optional[AllowUnknown[Unit]] = None


class Music(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    release_condition_id: Optional[int] = None
    categories: Optional[list[AllowUnknown[MusicCategory]]] = None
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
    music_difficulty: Optional[AllowUnknown[MusicDifficultyType]] = None
    play_level: Optional[int] = None
    release_condition_id: Optional[int] = None
    total_note_count: Optional[int] = None


class Character(Model):
    id: Optional[int] = None
    music_id: Optional[int] = None
    music_vocal_id: Optional[int] = None
    character_type: Optional[AllowUnknown[CharacterType]] = None
    character_id: Optional[int] = None
    seq: Optional[int] = None


class MusicVocal(Model):
    id: Optional[int] = None
    music_id: Optional[int] = None
    music_vocal_type: Optional[AllowUnknown[MusicVocalType]] = None
    seq: Optional[int] = None
    release_condition_id: Optional[int] = None
    caption: Optional[str] = None
    characters: Optional[list[Character]] = None
    asset_bundle_name: Optional[str] = None
    archive_published_at: Optional[datetime] = None
    special_season_id: Optional[int] = None
    archive_display_type: Optional[AllowUnknown[ArchiveDisplayType]] = None


class MusicDanceMember(Model):
    id: Optional[int] = None
    music_id: Optional[int] = None
    default_music_type: Optional[AllowUnknown[DefaultMusicType]] = None
    character_id1: Optional[int] = None
    unit1: Optional[AllowUnknown[Unit]] = None
    character_id2: Optional[int] = None
    unit2: Optional[AllowUnknown[Unit]] = None
    character_id3: Optional[int] = None
    unit3: Optional[AllowUnknown[Unit]] = None
    character_id4: Optional[int] = None
    unit4: Optional[AllowUnknown[Unit]] = None
    character_id5: Optional[int] = None
    unit5: Optional[AllowUnknown[Unit]] = None


class MusicAchievement(Model):
    id: Optional[int] = None
    music_achievement_type: Optional[AllowUnknown[MusicAchievementType]] = None
    music_achievement_type_value: Optional[str] = None
    resource_box_id: Optional[int] = None
    music_difficulty_type: Optional[AllowUnknown[MusicDifficultyType]] = None


class MusicVideoCharacter(Model):
    id: Optional[int] = None
    music_id: Optional[int] = None
    default_music_type: Optional[AllowUnknown[DefaultMusicType]] = None
    game_character_unit_id: Optional[int] = None
    dance_priority: Optional[int] = None
    seq: Optional[int] = None
    priority: Optional[int] = None


class MusicAssetVariant(Model):
    id: Optional[int] = None
    music_vocal_id: Optional[int] = None
    seq: Optional[int] = None
    music_asset_type: Optional[AllowUnknown[MusicAssetType]] = None
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
    release_condition_type: Optional[AllowUnknown[ReleaseConditionType]] = None
    release_condition_type_level: Optional[int] = None
    release_condition_type_id: Optional[int] = None
    release_condition_type_quantity: Optional[int] = None
    release_condition_type_id2: Optional[int] = None


class PlayLevelScore(Model):
    live_type: Optional[AllowUnknown[LiveType]] = None
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
    ingame_note_type: Optional[AllowUnknown[IngameNoteType]] = None
    score_coefficient: Optional[float] = None
    damage_bad: Optional[int] = None
    damage_miss: Optional[int] = None


class IngameNoteJudge(Model):
    id: Optional[int] = None
    ingame_note_jadge_type: Optional[AllowUnknown[IngameNoteJudgeType]] = None
    score_coefficient: Optional[float] = None
    damage: Optional[int] = None


class IngamePlayLevel(Model):
    play_level: Optional[int] = None
    score_coefficient: Optional[float] = None


class IngameCutin(Model):
    id: Optional[int] = None
    music_difficulty: Optional[AllowUnknown[MusicDifficultyType]] = None
    combo: Optional[int] = None


class IngameCutinCharacter(Model):
    id: Optional[int] = None
    ingame_cutin_character_type: Optional[AllowUnknown[IngameCutinCharacterType]] = None
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
    ingame_note_type: Optional[AllowUnknown[IngameNoteType]] = None
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
    live_type: Optional[AllowUnknown[LiveType]] = None
    ingame_note_jadge_type: Optional[AllowUnknown[IngameNoteJudgeType]] = None
    score: Optional[int] = None


class Shop(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    shop_type: Optional[AllowUnknown[ShopType]] = None
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
    costs: Optional[list[ShopItemCost]] = None
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
    costs: Optional[list[Costume3dShopItemCost]] = None
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
    target_unit: Optional[AllowUnknown[Unit]] = None
    target_card_attr: Optional[AllowUnknown[CardAttr]] = None
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
    material_type: Optional[AllowUnknown[MaterialType]] = None
    can_use: Optional[bool] = None
    flavor_text2: Optional[str] = None
    change_flavor_text_at: Optional[datetime] = None


class GachaCardRarityRate(Model):
    id: Optional[int] = None
    group_id: Optional[int] = None
    card_rarity_type: Optional[AllowUnknown[CardRarityType]] = None
    lottery_type: Optional[AllowUnknown[LotteryType]] = None
    rate: Optional[float] = None


class GachaDetail(Model):
    id: Optional[int] = None
    gacha_id: Optional[int] = None
    card_id: Optional[int] = None
    weight: Optional[int] = None
    is_wish: Optional[bool] = None
    gacha_detail_wish_type: Optional[AllowUnknown[GachaDetailWishType]] = None
    fixed_bonus_weight: Optional[int] = None


class GachaBehavior(Model):
    id: Optional[int] = None
    gacha_id: Optional[int] = None
    gacha_behavior_type: Optional[AllowUnknown[GachaBehaviorType]] = None
    cost_resource_type: Optional[AllowUnknown[ResourceType]] = None
    cost_resource_quantity: Optional[int] = None
    spin_count: Optional[int] = None
    execute_limit: Optional[int] = None
    group_id: Optional[int] = None
    priority: Optional[int] = None
    resource_category: Optional[AllowUnknown[ResourceCategory]] = None
    gacha_spinnable_type: Optional[AllowUnknown[GachaSpinnableType]] = None
    cost_resource_id: Optional[int] = None
    gacha_extra_id: Optional[int] = None


class GachaPickup(Model):
    id: Optional[int] = None
    gacha_id: Optional[int] = None
    card_id: Optional[int] = None
    gacha_pickup_type: Optional[AllowUnknown[GachaPickupType]] = None


class GachaInformation(Model):
    gacha_id: Optional[int] = None
    summary: Optional[str] = None
    description: Optional[str] = None


class Gacha(Model):
    id: Optional[int] = None
    gacha_type: Optional[AllowUnknown[GachaType]] = None
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
    gacha_card_rarity_rates: Optional[list[GachaCardRarityRate]] = None
    gacha_details: Optional[list[GachaDetail]] = None
    gacha_behaviors: Optional[list[GachaBehavior]] = None
    gacha_pickups: Optional[list[GachaPickup]] = None
    gacha_pickup_costumes: Optional[list[Empty]] = None
    gacha_information: Optional[GachaInformation] = None
    drawable_gacha_hour: Optional[int] = None
    gacha_bonus_id: Optional[int] = None
    spin_limit: Optional[int] = None
    gacha_bonus_item_receivable_reward_group_id: Optional[int] = None
    gacha_freebie_group_id: Optional[int] = None


class GachaBonus(Model):
    id: Optional[int] = None
    switch_fixed_bonus_weight: Optional[bool] = None


class GachaBonusPoint(Model):
    id: Optional[int] = None
    resource_type: Optional[AllowUnknown[ResourceType]] = None
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
    child_gacha_ids: Optional[list[int]] = None
    seq: Optional[int] = None
    asset_bundle_name: Optional[str] = None


class PracticeTicket(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    exp: Optional[int] = None
    flavor_text: Optional[str] = None
    character_id: Optional[int] = None


class SkillPracticeTicket(PracticeTicket):
    pass


class Level(Model):
    id: Optional[int] = None
    level_type: Optional[AllowUnknown[LevelType]] = None
    level: Optional[int] = None
    total_exp: Optional[int] = None


class Episode(Model):
    id: Optional[int] = None
    episode_no: Optional[int] = None
    title: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    scenario_id: Optional[str] = None
    release_condition_id: Optional[int] = None
    reward_resource_box_ids: Optional[list[int]] = None


class UnitStoryEpisode(Episode):
    unit: Optional[AllowUnknown[Unit]] = None
    chapter_no: Optional[int] = None
    unit_episode_category: Optional[AllowUnknown[Unit]] = None
    episode_no_label: Optional[str] = None
    limited_release_start_at: Optional[datetime] = None
    limited_release_end_at: Optional[datetime] = None
    and_release_condition_id: Optional[int] = None
    unit_story_episode_group_id: Optional[int] = None


class Chapter(Model):
    id: Optional[int] = None
    unit: Optional[AllowUnknown[Unit]] = None
    chapter_no: Optional[int] = None
    title: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    episodes: Optional[list[UnitStoryEpisode]] = None


class UnitStory(Model):
    unit: Optional[AllowUnknown[Unit]] = None
    seq: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    chapters: Optional[list[Chapter]] = None


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
    episodes: Optional[list[SpecialStoryEpisode]] = None


class Config(Model):
    config_key: Optional[str] = None
    value: Optional[str] = None


class ClientConfig(Model):
    id: Optional[int] = None
    value: Optional[str] = None
    type: Optional[AllowUnknown[ClientConfigType]] = None


class Wording(Model):
    wording_key: Optional[str] = None
    value: Optional[str] = None


class Costume3d(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    costume3d_group_id: Optional[int] = None
    costume3d_type: Optional[AllowUnknown[Costume3dType]] = None
    name: Optional[str] = None
    part_type: Optional[AllowUnknown[PartType]] = None
    color_id: Optional[int] = None
    color_name: Optional[str] = None
    character_id: Optional[int] = None
    costume3d_rarity: Optional[AllowUnknown[Costume3dRarity]] = None
    how_to_obtain: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    designer: Optional[str] = None
    archive_display_type: Optional[AllowUnknown[ArchiveDisplayType]] = None
    archive_published_at: Optional[datetime] = None
    published_at: Optional[datetime] = None


class Costume3dModel(Model):
    id: Optional[int] = None
    costume3d_id: Optional[int] = None
    unit: Optional[AllowUnknown[Unit]] = None
    head_costume3d_asset_bundle_type: Optional[AllowUnknown[HeadCostume3dAssetBundleType]] = None
    thumbnail_asset_bundle_name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    color_asset_bundle_name: Optional[str] = None
    part: Optional[str] = None


class Costume3dModelPattern(Model):
    id: Optional[int] = None
    head_costume3d_id: Optional[int] = None
    hair_costume3d_id: Optional[int] = None
    unit: Optional[AllowUnknown[Unit]] = None
    is_default: Optional[bool] = None


class GameCharacterUnit3dMotion(Model):
    id: Optional[int] = None
    game_character_unit_id: Optional[int] = None
    motion_type: Optional[AllowUnknown[MotionType]] = None
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
    topic_type: Optional[AllowUnknown[TopicType]] = None
    topic_type_id: Optional[int] = None
    release_condition_id: Optional[int] = None


class LiveStage(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class Stamp(Model):
    id: Optional[int] = None
    stamp_type: Optional[AllowUnknown[StampType]] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    balloon_asset_bundle_name: Optional[str] = None
    character_id1: Optional[int] = None
    game_character_unit_id: Optional[int] = None
    archive_published_at: Optional[datetime] = None
    description: Optional[str] = None
    archive_display_type: Optional[AllowUnknown[ArchiveDisplayType]] = None
    character_id2: Optional[int] = None


class MultiLiveLobby(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    photon_lobby_name: Optional[str] = None
    matching_logic: Optional[AllowUnknown[MatchingLogic]] = None
    total_power: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    multi_live_lobby_type: Optional[AllowUnknown[MultiLiveLobbyType]] = None


class MasterLessonCost(Cost):
    id: Optional[int] = None
    card_rarity_type: Optional[AllowUnknown[CardRarityType]] = None
    master_rank: Optional[int] = None
    seq: Optional[int] = None
    character_id: Optional[int] = None
    unit: Optional[AllowUnknown[Unit]] = None


class MasterLesson(Model):
    card_rarity_type: Optional[AllowUnknown[CardRarityType]] = None
    master_rank: Optional[int] = None
    power1_bonus_fixed: Optional[int] = None
    power2_bonus_fixed: Optional[int] = None
    power3_bonus_fixed: Optional[int] = None
    character_rank_exp: Optional[int] = None
    costs: Optional[list[MasterLessonCost]] = None
    rewards: Optional[list[Empty]] = None


class MasterLessonReward(Model):
    id: Optional[int] = None
    card_id: Optional[int] = None
    master_rank: Optional[int] = None
    seq: Optional[int] = None
    resource_box_id: Optional[int] = None
    card_rarity: Optional[int] = None


class CardExchangeResource(Model):
    card_rarity_type: Optional[AllowUnknown[CardRarityType]] = None
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
    refresh_cycle: Optional[AllowUnknown[RefreshCycle]] = None
    costs: Optional[list[MaterialExchangeCost]] = None
    exchange_limit: Optional[int] = None
    start_at: Optional[datetime] = None
    is_display_quantity: Optional[bool] = None
    display_name: Optional[str] = None
    thumbnail_asset_bundle_name: Optional[str] = None


class MaterialExchangeDisplayResourceGroup(Model):
    id: Optional[int] = None
    group_id: Optional[int] = None
    seq: Optional[int] = None
    resource_type: Optional[AllowUnknown[ResourceType]] = None
    resource_id: Optional[int] = None
    asset_bundle_name: Optional[str] = None


class MaterialExchangeFreebie(Model):
    id: Optional[int] = None
    material_exchange_freebie_group_id: Optional[int] = None
    material_exchange_freebie_type_id: Optional[int] = None
    resource_box_id: Optional[int] = None


class MaterialExchangeFreebieGroup(Model):
    id: Optional[int] = None
    material_exchange_freebie_type: Optional[AllowUnknown[MaterialExchangeFreebieType]] = None


class MaterialExchangeSummary(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    exchange_category: Optional[AllowUnknown[ExchangeCategory]] = None
    material_exchange_type: Optional[AllowUnknown[MaterialExchangeType]] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    start_at: Optional[datetime] = None
    material_exchanges: Optional[list[MaterialExchange]] = None
    end_at: Optional[datetime] = None
    notification_remain_hour: Optional[int] = None
    material_exchange_display_resource_groups: Optional[list[MaterialExchangeDisplayResourceGroup]] = None
    material_exchange_display_resource_group_id: Optional[int] = None
    material_exchange_freebie_group_json: Optional[MaterialExchangeFreebieGroup] = None
    material_exchange_freebies: Optional[list[MaterialExchangeFreebie]] = None


class BoostItem(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    recovery_value: Optional[int] = None
    asset_bundle_name: Optional[str] = None # = Field(None, alias="assetBundleName")
    flavor_text: Optional[str] = None


class BillingProduct(Model):
    id: Optional[int] = None
    group_id: Optional[int] = None
    platform: Optional[AllowUnknown[BillingPlatform]] = None
    product_id: Optional[str] = None
    price: Optional[int] = None
    unit_price: Optional[float] = None


class BillingShopItem(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    billing_shop_item_type: Optional[AllowUnknown[BillingShopItemType]] = None
    billing_product_group_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    billable_limit_type: Optional[AllowUnknown[BillableLimitType]] = None
    billable_limit_reset_interval_type: Optional[AllowUnknown[BillableLimitResetIntervalType]] = None
    asset_bundle_name: Optional[str] = None
    resource_box_id: Optional[int] = None
    billable_limit_value: Optional[int] = None
    bonus_resource_box_id: Optional[int] = None
    label: Optional[str] = None
    end_at: Optional[datetime] = None
    start_at: Optional[datetime] = None
    billable_limit_reset_interval_value: Optional[int] = None
    purchase_option: Optional[AllowUnknown[PurchaseOption]] = None
    sale_type: Optional[str] = None


class BillingShopItemExchangeCost(Cost):
    id: Optional[int] = None
    billing_shop_item_id: Optional[int] = None


class BillingShopItemGroup(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    seq: Optional[int] = None
    billing_shop_item_ids: Optional[list[int]] = None


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
    colorful_pass_tier: Optional[AllowUnknown[ColorfulPassTier]] = None
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
    jewel_behavior_type: Optional[AllowUnknown[JewelBehaviorType]] = None
    jewel_behavior_type_quantity: Optional[int] = None
    amount: Optional[int] = None


class CharacterRankAchieveResource(Model):
    release_condition_id: Optional[int] = None
    character_id: Optional[int] = None
    character_rank: Optional[int] = None
    resources: Optional[list[Empty]] = None


class CharacterRank(Model):
    id: Optional[int] = None
    character_id: Optional[int] = None
    character_rank: Optional[int] = None
    power1_bonus_rate: Optional[float] = None
    power2_bonus_rate: Optional[float] = None
    power3_bonus_rate: Optional[float] = None
    reward_resource_box_ids: Optional[list[int]] = None
    character_rank_achieve_resources: Optional[
        list[CharacterRankAchieveResource]
    ] = None


class CharacterMissionV2(Model):
    id: Optional[int] = None
    character_mission_type: Optional[AllowUnknown[CharacterMissionType]] = None
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
    character_mission_type: Optional[AllowUnknown[CharacterMissionType]] = None
    area_item_id: Optional[int] = None
    character_id: Optional[int] = None
    unit: Optional[AllowUnknown[Unit]] = None


class SystemLive2d(Live2d):
    serif: Optional[str] = None
    voice: Optional[str] = None
    published_at: Optional[datetime] = None
    closed_at: Optional[datetime] = None
    special_season_id: Optional[int] = None


class MissionReward(Model):
    id: Optional[int] = None
    mission_type: Optional[AllowUnknown[MissionType]] = None
    mission_id: Optional[int] = None
    seq: Optional[int] = None
    resource_box_id: Optional[int] = None


class NormalMission(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    normal_mission_type: Optional[AllowUnknown[NormalMissionType]] = None
    requirement: Optional[int] = None
    sentence: Optional[str] = None
    rewards: Optional[list[MissionReward]] = None


class BeginnerMission(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    beginner_mission_type: Optional[AllowUnknown[BeginnerMissionType]] = None
    beginner_mission_category: Optional[AllowUnknown[BeginnerMissionCategory]] = None
    condition_value: Optional[int] = None
    requirement: Optional[int] = None
    sentence: Optional[str] = None
    rewards: Optional[list[MissionReward]] = None


class Detail(Model):
    resource_box_purpose: Optional[AllowUnknown[ResourceBoxPurpose]] = None
    resource_box_id: Optional[int] = None
    seq: Optional[int] = None
    resource_type: Optional[AllowUnknown[ResourceType]] = None
    resource_quantity: Optional[int] = None
    resource_id: Optional[int] = None
    resource_level: Optional[int] = None


class ResourceBox(Model):
    resource_box_purpose: Optional[AllowUnknown[ResourceBoxPurpose]] = None
    id: Optional[int] = None
    resource_box_type: Optional[AllowUnknown[ResourceBoxType]] = None
    details: Optional[list[Detail]] = None
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
    live_mission_type: Optional[AllowUnknown[LiveMissionType]] = None
    requirement: Optional[int] = None
    rewards: Optional[list[MissionReward]] = None


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
    unit: Optional[AllowUnknown[Unit]] = None


class Penlight(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    default_penlight_color_id: Optional[int] = None
    asset_bundle_name: Optional[str] = None


class LiveTalk(Model):
    id: Optional[int] = None
    live_talk_type: Optional[AllowUnknown[LiveTalkType]] = None
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
        list[GachaCeilExchangeSubstituteCost]
    ] = None
    exchange_limit: Optional[int] = None
    gacha_ceil_exchange_label_type: Optional[AllowUnknown[GachaCeilExchangeLabelType]] = None
    substitute_limit: Optional[int] = None


class GachaCeilExchangeSummary(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    gacha_id: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    gacha_ceil_exchanges: Optional[list[GachaCeilExchange]] = None
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
    gacha_display_type: Optional[AllowUnknown[GachaDisplayType]] = None


class HonorGroup(Model):
    id: Optional[int] = None
    name: Optional[str] = None
    honor_type: Optional[AllowUnknown[HonorType]] = None
    background_asset_bundle_name: Optional[str] = None
    frame_name: Optional[str] = None


class HonorLevel(Model):
    honor_id: Optional[int] = None
    level: Optional[int] = None
    bonus: Optional[int] = None
    description: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    honor_rarity: Optional[AllowUnknown[HonorRarity]] = None


class Honor(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    group_id: Optional[int] = None
    honor_rarity: Optional[AllowUnknown[HonorRarity]] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    levels: Optional[list[HonorLevel]] = None
    honor_type_id: Optional[int] = None
    honor_mission_type: Optional[AllowUnknown[HonorMissionType]] = None


class HonorMission(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    honor_mission_type: Optional[AllowUnknown[HonorMissionType]] = None
    requirement: Optional[int] = None
    sentence: Optional[str] = None
    rewards: Optional[list[MissionReward]] = None


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
    honor_rarity: Optional[AllowUnknown[HonorRarity]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    levels: Optional[list[BondsHonorLevel]] = None
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
    bonds_reward_type: Optional[AllowUnknown[BondsRewardType]] = None
    resource_box_id: Optional[int] = None
    description: Optional[str] = None


class ChallengeLiveDetail(Model):
    id: Optional[int] = None
    challenge_live_id: Optional[int] = None
    challenge_live_type: Optional[AllowUnknown[LiveType]] = None


class ChallengeLive(Model):
    id: Optional[int] = None
    playable_count: Optional[int] = None
    challenge_live_details: Optional[list[ChallengeLiveDetail]] = None


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
    challenge_live_play_day_rewards: Optional[list[ChallengeLivePlayDayReward]] = None


class VirtualLiveSetlist(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    seq: Optional[int] = None
    virtual_live_setlist_type: Optional[AllowUnknown[VirtualLiveSetlistType]] = None
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
    day_of_week: Optional[AllowUnknown[DayOfWeek]] = None
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
    virtual_live_performance_type: Optional[AllowUnknown[VirtualLivePerformanceType]] = None


class VirtualLiveReward(Model):
    id: Optional[int] = None
    virtual_live_type: Optional[AllowUnknown[VirtualLiveType]] = None
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
    virtual_item_category: Optional[AllowUnknown[VirtualItemCategory]] = None
    seq: Optional[int] = None
    priority: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    cost_virtual_coin: Optional[int] = None
    cost_jewel: Optional[int] = None
    cheer_point: Optional[int] = None
    effect_asset_bundle_name: Optional[str] = None
    effect_expression_type: Optional[AllowUnknown[EffectExpressionType]] = None
    unit: Optional[AllowUnknown[Unit]] = None
    game_character_unit_id: Optional[int] = None
    virtual_item_label_type: Optional[AllowUnknown[VirtualItemLabelType]] = None


class VirtualLiveAppeal(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    virtual_live_stage_status: Optional[AllowUnknown[VirtualLiveStageStatus]] = None
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
    virtual_live_type: Optional[AllowUnknown[VirtualLiveType]] = None
    virtual_live_platform: Optional[str] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    screen_mv_music_vocal_id: Optional[int] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    ranking_announce_at: Optional[datetime] = None
    virtual_live_setlists: Optional[list[VirtualLiveSetlist]] = None
    virtual_live_beginner_schedules: Optional[
        list[VirtualLiveBeginnerSchedule]
    ] = None
    virtual_live_schedules: Optional[list[VirtualLiveSchedule]] = None
    virtual_live_characters: Optional[list[VirtualLiveCharacter]] = None
    virtual_live_reward: Optional[VirtualLiveReward] = None
    virtual_live_rewards: Optional[list[VirtualLiveReward]] = None
    virtual_live_cheer_point_rewards: Optional[list[Empty]] = None
    virtual_live_waiting_room: Optional[VirtualLiveWaitingRoom] = None
    virtual_items: Optional[list[VirtualItem]] = None
    virtual_live_appeals: Optional[list[VirtualLiveAppeal]] = None
    virtual_live_background_musics: Optional[list[VirtualLiveBackgroundMusic]] = None
    virtual_live_information: Optional[VirtualLiveInformation] = None
    archive_release_condition_id: Optional[int] = None
    virtual_live_ticket_id: Optional[int] = None


class VirtualShopItem(Model):
    id: Optional[int] = None
    virtual_shop_id: Optional[int] = None
    virtual_shop_item_type: Optional[AllowUnknown[VirtualShopItemType]] = None
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
    virtual_shop_items: Optional[list[VirtualShopItem]] = None
    virtual_shop_type: Optional[AllowUnknown[VirtualShopType]] = None
    virtual_live_id: Optional[int] = None


class PaidVirtualLiveShopCost(Model):
    id: Optional[int] = None
    cost_resource_type: Optional[AllowUnknown[ResourceType]] = None
    cost_resource_quantity: Optional[int] = None
    start_at: Optional[datetime] = None


class PaidVirtualLiveShopItem(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    paid_virtual_live_shop_item_group_id: Optional[int] = None
    name: Optional[str] = None
    resource_box_id: Optional[int] = None
    paid_virtual_live_shop_item_purchase_type: Optional[
        AllowUnknown[PaidVirtualLiveShopItemPurchaseType]] = None
    paid_virtual_live_shop_costs: Optional[list[PaidVirtualLiveShopCost]] = None
    asset_bundle_name: Optional[str] = None
    description: Optional[str] = None


class PaidVirtualLiveShopItemGroup(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    paid_virtual_live_shop_item_ids: Optional[list[int]] = None
    name: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class PaidVirtualLive(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    virtual_live_part: Optional[int] = None
    paid_virtual_live_type: Optional[AllowUnknown[PaidVirtualLiveType]] = None
    units: Optional[list[AllowUnknown[Unit]]] = None
    icon_asset_bundle_name: Optional[str] = None
    background_asset_bundle_name: Optional[str] = None


class VirtualLiveCheerMessage(Model):
    id: Optional[int] = None
    virtual_live_type: Optional[AllowUnknown[VirtualLiveType]] = None
    resource_type: Optional[AllowUnknown[ResourceType]] = None
    from_cost_virtual_coin: Optional[int] = None
    to_cost_virtual_coin: Optional[int] = None
    from_cost: Optional[int] = None
    to_cost: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    message_length_limit: Optional[int] = None
    display_sec: Optional[float] = None
    message_size: Optional[AllowUnknown[MessageSize]] = None
    color_code: Optional[str] = None
    virtual_live_cheer_message_display_limit_id: Optional[int] = None


class VirtualLiveCheerMessageDisplayLimit(Model):
    id: Optional[int] = None
    display_limit: Optional[int] = None


class VirtualLiveTicket(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    virtual_live_ticket_type: Optional[AllowUnknown[VirtualLiveTicketType]] = None
    name: Optional[str] = None
    flavor_text: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    virtual_live_schedule_id: Optional[int] = None


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
    part: Optional[AllowUnknown[AccessoryPart]] = None
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
    accessory_part: Optional[AllowUnknown[AccessoryPart]] = None
    accessory_asset_bundle_name: Optional[str] = None


class NgWord(Model):
    id: Optional[int] = None
    word: Optional[str] = None


class RuleSlide(Model):
    id: Optional[int] = None
    rule_slide_type: Optional[AllowUnknown[RuleSlideType]] = None
    asset_bundle_name: Optional[str] = None


class Facility(Model):
    id: Optional[int] = None
    facility_type: Optional[AllowUnknown[FacilityType]] = None
    release_condition_id: Optional[int] = None
    and_release_condition_id: Optional[int] = None


class OneTimeBehavior(Model):
    id: Optional[int] = None
    one_time_behavior_type: Optional[AllowUnknown[OneTimeBehaviorType]] = None
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
    limited_login_bonus_details: Optional[list[LimitedLoginBonusDetail]] = None


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
    event_ranking_rewards: Optional[list[EventRankingReward]] = None
    is_to_rank_border: Optional[bool] = None


class Event(Model):
    id: Optional[int] = None
    event_type: Optional[AllowUnknown[EventType]] = None
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
    unit: Optional[AllowUnknown[Unit]] = None
    event_ranking_reward_ranges: Optional[list[EventRankingRewardRange]] = None
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
    card_attr: Optional[AllowUnknown[CardAttr]] = None
    bonus_rate: Optional[float] = None


class EventRarityBonusRate(Model):
    id: Optional[int] = None
    card_rarity_type: Optional[AllowUnknown[CardRarityType]] = None
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
    story_type: Optional[AllowUnknown[StoryType]] = None
    resource_box_id: Optional[int] = None


class EventStoryEpisode(Model):
    id: Optional[int] = None
    event_story_id: Optional[int] = None
    episode_no: Optional[int] = None
    title: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    scenario_id: Optional[str] = None
    release_condition_id: Optional[int] = None
    episode_rewards: Optional[list[EpisodeReward]] = None
    game_character_id: Optional[int] = None


class EventStory(Model):
    id: Optional[int] = None
    event_id: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    event_story_episodes: Optional[list[EventStoryEpisode]] = None
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
    event_exchanges: Optional[list[EventExchange]] = None


class EventStoryUnit(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    event_story_id: Optional[int] = None
    unit: Optional[AllowUnknown[Unit]] = None
    event_story_unit_relation: Optional[AllowUnknown[EventStoryUnitRelation]] = None


class EventCard(Model):
    id: Optional[int] = None
    card_id: Optional[int] = None
    event_id: Optional[int] = None
    bonus_rate: Optional[float] = None
    is_display_card_story: Optional[bool] = None


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
    preliminary_tournament_type: Optional[AllowUnknown[PreliminaryTournamentType]] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    release_condition_id: Optional[int] = None
    preliminary_tournament_cards: Optional[list[PreliminaryTournamentCard]] = None
    preliminary_tournament_musics: Optional[list[PreliminaryTournamentMusic]] = None


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
        AllowUnknown[CheerfulCarnivalTeamPointTermType]] = None
    cheerful_carnival_result_type: Optional[AllowUnknown[CheerfulCarnivalResultType]] = None
    resource_box_id: Optional[int] = None


class Appeal(Model):
    id: Optional[int] = None
    seq: Optional[int] = None
    appeal_target_type: Optional[AllowUnknown[AppealTargetType]] = None
    appeal_type: Optional[AllowUnknown[AppealType]] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    appeal_read_condition_type: Optional[AllowUnknown[AppealReadConditionType]] = None
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
    story_type: Optional[AllowUnknown[StoryType]] = None
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
    custom_profile_resource_type: Optional[AllowUnknown[CustomProfileResourceType]] = None
    id: Optional[int] = None
    seq: Optional[int] = None
    name: Optional[str] = None
    resource_load_type: Optional[AllowUnknown[ResourceLoadType]] = None
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
        AllowUnknown[CustomProfileResourceCollectionType]] = None


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
    cost_resource_type: Optional[AllowUnknown[ResourceType]] = None
    cost_resource_quantity: Optional[int] = None
    spin_count: Optional[int] = None


class CustomProfileGachaDetail(Model):
    id: Optional[int] = None
    custom_profile_gacha_id: Optional[int] = None
    custom_profile_resource_type: Optional[AllowUnknown[CustomProfileResourceType]] = None
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
    custom_profile_gacha_behaviors: Optional[list[CustomProfileGachaBehavior]] = None
    custom_profile_gacha_details: Optional[list[CustomProfileGachaDetail]] = None


class CustomProfileGachaTab(Model):
    id: Optional[int] = None
    child_custom_profile_gacha_ids: Optional[list[int]] = None
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
    character_ids: Optional[list[int]] = None
    music_id: Optional[int] = None


class StreamingLiveArchive(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    virtual_live_part: Optional[int] = None
    streaming_live_category_id: Optional[int] = None
    streaming_live_setlists: Optional[list[StreamingLiveSetlist]] = None
    play_time: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class StreamingLiveCategoryItem(Model):
    id: Optional[int] = None
    name: Optional[str] = None


class Omikuji(Model):
    id: Optional[int] = None
    omikuji_group_id: Optional[int] = None
    unit: Optional[AllowUnknown[Unit]] = None
    fortune_type: Optional[AllowUnknown[FortuneType]] = None
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
    fortune_type: Optional[AllowUnknown[FortuneType]] = None
    rate: Optional[float] = None


class OmikujiCost(Cost):
    id: Optional[int] = None
    omikuji_group_id: Optional[int] = None
    seq: Optional[int] = None


class OmikujiReward(Model):
    id: Optional[int] = None
    omikuji_group_id: Optional[int] = None
    seq: Optional[int] = None
    resource_type: Optional[AllowUnknown[ResourceType]] = None
    resource_id: Optional[int] = None
    resource_quantity: Optional[int] = None


class VirtualBoothShop(Model):
    id: Optional[int] = None
    virtual_live_id: Optional[int] = None
    virtual_booth_shop_type: Optional[AllowUnknown[VirtualBoothShopType]] = None
    target_id: Optional[int] = None


class SpecialSeason(Model):
    id: Optional[int] = None
    special_season_type: Optional[AllowUnknown[SpecialSeasonType]] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    priority: Optional[int] = None


class SpecialSeasonArea(Model):
    id: Optional[int] = None
    special_season_id: Optional[int] = None
    area_id: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    file_name: Optional[str] = None
    special_season_area_use_type: Optional[AllowUnknown[SpecialSeasonAreaUseType]] = None


class RankMatchPenalty(Model):
    id: Optional[int] = None
    count: Optional[int] = None
    rank_match_penalty_type: Optional[AllowUnknown[RankMatchPenaltyType]] = None
    rank_match_penalty_type_value: Optional[int] = None


class RankMatchPlacement(Model):
    id: Optional[int] = None
    rank_match_placement_condition_type: Optional[str] = None
    tier_behavior_type: Optional[AllowUnknown[TierBehaviorType]] = None
    tier_behavior_type_value: Optional[int] = None
    rank_match_placement_condition_type_value: Optional[int] = None


class RankMatchBonusPointCondition(Model):
    id: Optional[int] = None
    rank_match_bonus_point_condition_type: Optional[AllowUnknown[RankMatchBonusPointConditionType]] = None
    group_id: Optional[int] = None
    priority: Optional[int] = None
    calc_type: Optional[AllowUnknown[CalcType]] = None
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
        list[RankMatchSeasonPlayableTime]
    ] = None
    rank_match_season_tier_music_play_levels: Optional[
        list[RankMatchSeasonTierMusicPlayLevel]
    ] = None
    rank_match_season_tier_rewards: Optional[list[RankMatchSeasonTierReward]] = None
    demotion_flag: Optional[bool] = None


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
    panel_mission_type: Optional[AllowUnknown[PanelMissionType]] = None
    requirement1: Optional[int] = None
    rewards: Optional[list[MissionReward]] = None
    requirement2: Optional[int] = None


class MissionSheetReward(MissionReward):
    worksheet_version: Optional[str] = None


class PanelMissionSheet(Model):
    id: Optional[int] = None
    panel_mission_sheet_group_id: Optional[int] = None
    name: Optional[str] = None
    seq: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    panel_missions: Optional[list[PanelMission]] = None
    rewards: Optional[list[MissionSheetReward]] = None


class PanelMissionSheetGroup(Model):
    id: Optional[int] = None
    panel_mission_campaign_id: Optional[int] = None
    name: Optional[str] = None
    selectable_limit: Optional[int] = None
    seq: Optional[int] = None
    panel_mission_sheets: Optional[list[PanelMissionSheet]] = None


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
    panel_mission_sheet_groups: Optional[list[PanelMissionSheetGroup]] = None
    distribution_end_at: Optional[datetime] = None


class EventMission(Model):
    id: Optional[int] = None
    event_id: Optional[int] = None
    seq: Optional[int] = None
    event_mission_type: Optional[AllowUnknown[EventMissionType]] = None
    event_mission_category: Optional[AllowUnknown[EventMissionCategory]] = None
    requirement1: Optional[int] = None
    sentence: Optional[str] = None
    rewards: Optional[list[MissionReward]] = None
    requirement2: Optional[int] = None
    event_mission_selectable_reward_group_id: Optional[int] = None


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
    beginner_mission_v2_type: Optional[AllowUnknown[BeginnerMissionType]] = None
    beginner_mission_v2_category: Optional[AllowUnknown[BeginnerMissionCategory]] = None
    condition_value: Optional[int] = None
    requirement: Optional[int] = None
    sentence: Optional[str] = None
    rewards: Optional[list[MissionReward]] = None


class CharacterMissionV2ExJson(Model):
    id: Optional[int] = None
    character_mission_type: Optional[AllowUnknown[CharacterMissionType]] = None
    character_mission_ex_type: Optional[AllowUnknown[CharacterMissionType]] = None
    resource_type: Optional[AllowUnknown[ResourceType]] = None


class FriendInvitationCampaignMissionReward(Model):
    id: Optional[int] = None
    count_group_id: Optional[int] = None
    count: Optional[int] = None
    resource_box_id: Optional[int] = None


class FriendInvitationCampaignMission(Model):
    id: Optional[int] = None
    mission_type: Optional[AllowUnknown[FriendInvitationCampaignMissionType]] = None
    mission_category_id: Optional[int] = None
    name: Optional[str] = None
    requirement: Optional[int] = None
    reward: Optional[list[FriendInvitationCampaignMissionReward]] = None


class FriendInvitationCampaign(Model):
    id: Optional[int] = None
    group_id: Optional[int] = None
    title: Optional[str] = None
    asset_bundle_name: Optional[str] = None
    start_at: Optional[datetime] = None
    progress_end_at: Optional[datetime] = None
    receive_reward_end_at: Optional[int] = None
    closed_at: Optional[int] = None
    missions: Optional[list[FriendInvitationCampaignMission]] = None


class UnitStoryEpisodeGroup(Model):
    id: Optional[int] = None
    unit: Optional[AllowUnknown[Unit]] = None
    unit_episode_category: Optional[AllowUnknown[Unit]] = None
    outline: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class EpisodeBackgroundMusic(Model):
    id: Optional[int] = None
    story_type: Optional[AllowUnknown[StoryType]] = None
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
        AllowUnknown[WorldBloomSupportDeckCharacterType]] = None
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
    card_rarity_type: Optional[AllowUnknown[CardRarityType]] = None
    world_bloom_support_deck_character_bonuses: Optional[
        list[WorldBloomSupportDeckCharacterBonus]] = None
    world_bloom_support_deck_master_rank_bonuses: Optional[
        list[WorldBloomSupportDeckMasterRankBonus]] = None
    world_bloom_support_deck_skill_level_bonuses: Optional[
        list[WorldBloomSupportDeckSkillLevelBonus]] = None


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
    unit: Optional[AllowUnknown[Unit]] = None
    character_archive_voice_type: Optional[AllowUnknown[CharacterArchiveVoiceType]] = None
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
    character_archive_voice_tag_type: Optional[AllowUnknown[CharacterArchiveVoiceTagType]] = None
    name: Optional[str] = None


class LiveClearVoice(Model):
    id: Optional[int] = None
    game_character_unit_id: Optional[int] = None
    is_next_grade: Optional[bool] = None
    live_clear_voice_type: Optional[AllowUnknown[LiveClearVoiceType]] = None
    voice_file_name: Optional[str] = None


class AdReward(Model):
    id: Optional[int] = None
    ad_reward_play_type: Optional[AllowUnknown[AdRewardPlayType]] = None
    resource_box_id: Optional[int] = None
    live_bonus_count: Optional[int] = None
    daily_limit_count: Optional[int] = None
    display_flg: Optional[bool] = None
    start_at: Optional[int] = None
    end_at: Optional[int] = None


class CardSupply(Model):
    id: Optional[int] = None
    card_supply_type: Optional[AllowUnknown[CardSupplyType]] = None
    asset_bundle_name: Optional[str] = None


class CardSupplyGroup(Model):
    id: Optional[int] = None
    group_id: Optional[int] = None
    card_supply_id: Optional[int] = None


class EventMissionSelectableRewards(Model):
    id: Optional[int] = None
    resource_box_id: Optional[int] = None
    group_id: Optional[int] = None


class AreaSpiritWorldTreeReactionLottery(Model):
    id: Optional[int] = None
    area_spirit_world_tree_id: Optional[int] = None
    flavor_text: Optional[str] = None
    weight: Optional[int] = None
    asset_bundle_name: Optional[str] = None
    cue_name: Optional[str] = None


class AreaSpiritWorldTree(Model):
    id: Optional[int] = None
    area_id: Optional[int] = None
    seq: Optional[int] = None
    display_assetbundle_name: Optional[str] = None
    release_condition_id1: Optional[int] = None
    release_condition_id2: Optional[int] = None
    area_spirit_world_tree_reaction_lotteries: Optional[list[AreaSpiritWorldTreeReactionLottery]] = None


class HonorMissionTypeOrder(Model):
    id: Optional[int] = None
    honor_mission_type: Optional[AllowUnknown[HonorMissionType]] = None
    seq: Optional[int] = None


class GachaBonusItemReceivableReward(Model):
    id: Optional[int] = None
    group_id: Optional[int] = None
    gachaBonusBorderPoint: Optional[int] = None
    gachaBonusRewardType: Optional[AllowUnknown[GachaBonusRewardType]] = None
    resource_box_id: Optional[int] = None
    cardSupplyGroupId: Optional[int] = None
    description: Optional[str] = None
    asset_bundle_name: Optional[str] = None


class GachaFreebieGroup(Model):
    id: Optional[int] = None
    group_id: Optional[int] = None
    seq: Optional[int] = None
    resource_box_id: Optional[int] = None
    rarity: Optional[int] = None
    weight: Optional[int] = None


class HomeExchangeButton(Model):
    id: Optional[int] = None
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    asset_bundle_name: Optional[str] = None


class MaterialAutoExchangeMusicVocal(Model):
    id: Optional[int] = None
    material_id: Optional[int] = None
    music_vocal_id: Optional[int] = None
    obtain_at: Optional[datetime] = None


class ReleaseConditionLogicalExpression(Model):
    id: Optional[int] = None
    enable_release_condition_id1: Optional[int] = None
    enable_release_condition_id2: Optional[int] = None
    disable_release_condition_id: Optional[int] = None


class ActionSetLotteryCondition(Model):
    id: Optional[int] = None
    action_set_id: Optional[int] = None
    release_condition_logical_expression_id: Optional[int] = None
    release_condition_logical_expression_flag: Optional[bool] = None


class StoryMission(Model):
    id: Optional[int] = None
    requirement: Optional[int] = None
    resource_box_id: Optional[int] = None


class MasterData(Model):
    game_characters: Optional[list[GameCharacter]] = None
    game_character_units: Optional[list[GameCharacterUnit]] = None
    outside_characters: Optional[list[OutsideCharacter]] = None
    character3ds: Optional[list[Character3d]] = None
    character2ds: Optional[list[Character2d]] = None
    character_profiles: Optional[list[CharacterProfile]] = None
    bonds: Optional[list[Bond]] = None
    bonds_live2ds: Optional[list[BondsLive2d]] = None
    bonds_rank_up_live2ds: Optional[list[BondsRankUpLive2d]] = None
    unit_profiles: Optional[list[UnitProfile]] = None
    action_sets: Optional[list[ActionSet]] = None
    areas: Optional[list[Area]] = None
    area_playlists: Optional[list[AreaPlaylist]] = None
    mob_characters: Optional[list[MobCharacter]] = None
    character_costumes: Optional[list[CharacterCostume]] = None
    card_costume3ds: Optional[list[CardCostume3d]] = None
    cards: Optional[list[Card]] = None
    skills: Optional[list[Skill]] = None
    card_episodes: Optional[list[CardEpisode]] = None
    card_rarities: Optional[list[CardRarity]] = None
    card_skill_costs: Optional[list[CardSkillCost]] = None
    musics: Optional[list[Music]] = None
    music_tags: Optional[list[MusicTag]] = None
    music_difficulties: Optional[list[MusicDifficulty]] = None
    music_vocals: Optional[list[MusicVocal]] = None
    music_dance_members: Optional[list[MusicDanceMember]] = None
    music_achievements: Optional[list[MusicAchievement]] = None
    music_video_characters: Optional[list[MusicVideoCharacter]] = None
    music_asset_variants: Optional[list[MusicAssetVariant]] = None
    music_collaborations: Optional[list[MusicCollaboration]] = None
    episode_music_video_costumes: Optional[list[EpisodeMusicVideoCostume]] = None
    music_originals: Optional[list[MusicOriginal]] = None
    release_conditions: Optional[list[ReleaseCondition]] = None
    play_level_scores: Optional[list[PlayLevelScore]] = None
    ingame_combos: Optional[list[IngameCombo]] = None
    ingame_notes: Optional[list[IngameNote]] = None
    ingame_note_judges: Optional[list[IngameNoteJudge]] = None
    ingame_play_levels: Optional[list[IngamePlayLevel]] = None
    ingame_cutins: Optional[list[IngameCutin]] = None
    ingame_cutin_characters: Optional[list[IngameCutinCharacter]] = None
    ingame_judge_frames: Optional[list[IngameJudgeFrame]] = None
    ingame_note_judge_technical_scores: Optional[
        list[IngameNoteJudgeTechnicalScore]
    ] = None
    shops: Optional[list[Shop]] = None
    shop_items: Optional[list[ShopItem]] = None
    costume3d_shop_items: Optional[list[Costume3dShopItem]] = None
    area_items: Optional[list[AreaItem]] = None
    area_item_levels: Optional[list[AreaItemLevel]] = None
    materials: Optional[list[Material]] = None
    gachas: Optional[list[Gacha]] = None
    gacha_bonuses: Optional[list[GachaBonus]] = None
    gacha_bonus_points: Optional[list[GachaBonusPoint]] = None
    gacha_extras: Optional[list[GachaExtra]] = None
    gift_gacha_exchanges: Optional[list[GiftGachaExchange]] = None
    gacha_tabs: Optional[list[GachaTab]] = None
    practice_tickets: Optional[list[PracticeTicket]] = None
    skill_practice_tickets: Optional[list[SkillPracticeTicket]] = None
    levels: Optional[list[Level]] = None
    unit_stories: Optional[list[UnitStory]] = None
    special_stories: Optional[list[SpecialStory]] = None
    configs: Optional[list[Config]] = None
    client_configs: Optional[list[ClientConfig]] = None
    wordings: Optional[list[Wording]] = None
    costume3ds: Optional[list[Costume3d]] = None
    costume3d_models: Optional[list[Costume3dModel]] = None
    costume3d_model_available_patterns: Optional[
        list[Costume3dModelPattern]
    ] = None
    game_character_unit3d_motions: Optional[list[GameCharacterUnit3dMotion]] = None
    costume2ds: Optional[list[Costume2d]] = None
    costume2d_groups: Optional[list[Costume2dGroup]] = None
    topics: Optional[list[Topic]] = None
    live_stages: Optional[list[LiveStage]] = None
    stamps: Optional[list[Stamp]] = None
    multi_live_lobbies: Optional[list[MultiLiveLobby]] = None
    master_lessons: Optional[list[MasterLesson]] = None
    master_lesson_rewards: Optional[list[MasterLessonReward]] = None
    card_exchange_resources: Optional[list[CardExchangeResource]] = None
    material_exchanges: Optional[list[MaterialExchange]] = None
    material_exchange_summaries: Optional[list[MaterialExchangeSummary]] = None
    boost_items: Optional[list[BoostItem]] = None
    billing_products: Optional[list[BillingProduct]] = None
    billing_shop_items: Optional[list[BillingShopItem]] = None
    billing_shop_item_exchange_costs: Optional[
        list[BillingShopItemExchangeCost]
    ] = None
    billing_shop_item_groups: Optional[list[BillingShopItemGroup]] = None
    colorful_passes: Optional[list[ColorfulPass]] = None
    colorful_pass_v2s: Optional[list[ColorfulPassV2]] = None
    jewel_behaviors: Optional[list[JewelBehavior]] = None
    character_ranks: Optional[list[CharacterRank]] = None
    character_mission_v2s: Optional[list[CharacterMissionV2]] = None
    character_mission_v2_parameter_groups: Optional[
        list[CharacterMissionV2ParameterGroup]
    ] = None
    character_mission_v2_area_items: Optional[list[CharacterMissionV2AreaItem]] = None
    system_live2ds: Optional[list[SystemLive2d]] = None
    normal_missions: Optional[list[NormalMission]] = None
    beginner_missions: Optional[list[BeginnerMission]] = None
    resource_boxes: Optional[list[ResourceBox]] = None
    live_mission_periods: Optional[list[LiveMissionPeriod]] = None
    live_missions: Optional[list[LiveMission]] = None
    live_mission_passes: Optional[list[LiveMissionPass]] = None
    penlight_colors: Optional[list[PenlightColor]] = None
    penlights: Optional[list[Penlight]] = None
    live_talks: Optional[list[LiveTalk]] = None
    tips: Optional[list[Tip]] = None
    gacha_ceil_items: Optional[list[GachaCeilItem]] = None
    gacha_ceil_exchange_summaries: Optional[list[GachaCeilExchangeSummary]] = None
    player_rank_rewards: Optional[list[PlayerRankReward]] = None
    gacha_tickets: Optional[list[GachaTicket]] = None
    honor_groups: Optional[list[HonorGroup]] = None
    honors: Optional[list[Honor]] = None
    honor_missions: Optional[list[HonorMission]] = None
    bonds_honors: Optional[list[BondsHonor]] = None
    bonds_honor_words: Optional[list[BondsHonorWord]] = None
    bonds_rewards: Optional[list[BondsReward]] = None
    challenge_lives: Optional[list[ChallengeLive]] = None
    challenge_live_decks: Optional[list[ChallengeLiveDeck]] = None
    challenge_live_stages: Optional[list[ChallengeLiveStage]] = None
    challenge_live_stage_exs: Optional[list[ChallengeLiveStageEx]] = None
    challenge_live_high_score_rewards: Optional[
        list[ChallengeLiveHighScoreReward]
    ] = None
    challenge_live_characters: Optional[list[ChallengeLiveCharacter]] = None
    challenge_live_play_day_reward_periods: Optional[
        list[ChallengeLivePlayDayRewardPeriod]
    ] = None
    virtual_lives: Optional[list[VirtualLive]] = None
    virtual_shops: Optional[list[VirtualShop]] = None
    paid_virtual_live_shop_items: Optional[list[PaidVirtualLiveShopItem]] = None
    paid_virtual_live_shop_item_groups: Optional[
        list[PaidVirtualLiveShopItemGroup]
    ] = None
    paid_virtual_lives: Optional[list[PaidVirtualLive]] = None
    virtual_items: Optional[list[VirtualItem]] = None
    virtual_live_cheer_messages: Optional[list[VirtualLiveCheerMessage]] = None
    virtual_live_cheer_message_display_limits: Optional[
        list[VirtualLiveCheerMessageDisplayLimit]
    ] = None
    virtual_live_tickets: Optional[list[VirtualLiveTicket]] = None
    virtual_live_pamphlets: Optional[list[VirtualLivePamphlet]] = None
    avatar_accessories: Optional[list[AvatarAccessory]] = None
    avatar_costumes: Optional[list[AvatarCostume]] = None
    avatar_motions: Optional[list[AvatarMotion]] = None
    avatar_skin_colors: Optional[list[AvatarSkinColor]] = None
    avatar_coordinates: Optional[list[AvatarCoordinate]] = None
    ng_words: Optional[list[NgWord]] = None
    rule_slides: Optional[list[RuleSlide]] = None
    facilities: Optional[list[Facility]] = None
    one_time_behaviors: Optional[list[OneTimeBehavior]] = None
    login_bonuses: Optional[list[LoginBonus]] = None
    beginner_login_bonuses: Optional[list[BeginnerLoginBonus]] = None
    beginner_login_bonus_summaries: Optional[list[BeginnerLoginBonusSummary]] = None
    limited_login_bonuses: Optional[list[LimitedLoginBonus]] = None
    login_bonus_live2ds: Optional[list[LoginBonusLive2d]] = None
    events: Optional[list[Event]] = None
    event_musics: Optional[list[EventMusic]] = None
    event_deck_bonuses: Optional[list[EventDeckBonus]] = None
    event_rarity_bonus_rates: Optional[list[EventRarityBonusRate]] = None
    event_items: Optional[list[EventItem]] = None
    event_stories: Optional[list[EventStory]] = None
    event_exchange_summaries: Optional[list[EventExchangeSummary]] = None
    event_story_units: Optional[list[EventStoryUnit]] = None
    event_cards: Optional[list[EventCard]] = None
    preliminary_tournaments: Optional[list[PreliminaryTournament]] = None
    cheerful_carnival_summaries: Optional[list[CheerfulCarnivalSummary]] = None
    cheerful_carnival_teams: Optional[list[CheerfulCarnivalTeam]] = None
    cheerful_carnival_party_names: Optional[list[CheerfulCarnivalPartyName]] = None
    cheerful_carnival_character_party_names: Optional[
        list[CheerfulCarnivalCharacterPartyName]
    ] = None
    cheerful_carnival_live_team_point_bonuses: Optional[
        list[CheerfulCarnivalLiveTeamPointBonus]
    ] = None
    cheerful_carnival_rewards: Optional[list[CheerfulCarnivalReward]] = None
    cheerful_carnival_result_rewards: Optional[
        list[CheerfulCarnivalResultReward]
    ] = None
    appeals: Optional[list[Appeal]] = None
    boosts: Optional[list[Boost]] = None
    boost_presents: Optional[list[BoostPresent]] = None
    boost_present_costs: Optional[list[BoostPresentCost]] = None
    episode_characters: Optional[list[EpisodeCharacter]] = None
    custom_profile_text_colors: Optional[list[CustomProfileTextColor]] = None
    custom_profile_text_fonts: Optional[list[CustomProfileTextFont]] = None
    custom_profile_player_info_resources: Optional[
        list[CustomProfilePlayerInfoResource]
    ] = None
    custom_profile_general_background_resources: Optional[
        list[CustomProfileGeneralBackgroundResource]
    ] = None
    custom_profile_story_background_resources: Optional[
        list[CustomProfileStoryBackgroundResource]
    ] = None
    custom_profile_collection_resources: Optional[
        list[CustomProfileCollectionResource]
    ] = None
    custom_profile_member_standing_picture_resources: Optional[
        list[CustomProfileMemberStandingPictureResource]
    ] = None
    custom_profile_shape_resources: Optional[list[CustomProfileShapeResource]] = None
    custom_profile_etc_resources: Optional[list[CustomProfileEtcResource]] = None
    custom_profile_member_resource_exclude_cards: Optional[list[Empty]] = None
    custom_profile_gachas: Optional[list[CustomProfileGacha]] = None
    custom_profile_gacha_tabs: Optional[list[CustomProfileGachaTab]] = None
    streaming_live_bgms: Optional[list[StreamingLiveBgm]] = None
    streaming_live_archives: Optional[list[StreamingLiveArchive]] = None
    streaming_live_category: Optional[list[StreamingLiveCategoryItem]] = None
    omikujis: Optional[list[Omikuji]] = None
    omikuji_groups: Optional[list[OmikujiGroup]] = None
    omikuji_rates: Optional[list[OmikujiRate]] = None
    omikuji_costs: Optional[list[OmikujiCost]] = None
    omikuji_rewards: Optional[list[OmikujiReward]] = None
    virtual_booth_shops: Optional[list[VirtualBoothShop]] = None
    special_seasons: Optional[list[SpecialSeason]] = None
    special_season_areas: Optional[list[SpecialSeasonArea]] = None
    rank_match_penalties: Optional[list[RankMatchPenalty]] = None
    rank_match_placements: Optional[list[RankMatchPlacement]] = None
    rank_match_bonus_point_conditions: Optional[
        list[RankMatchBonusPointCondition]
    ] = None
    rank_match_seasons: Optional[list[RankMatchSeason]] = None
    rank_match_tiers: Optional[list[RankMatchTier]] = None
    rank_match_tier_bonus_points: Optional[list[RankMatchTierBonusPoint]] = None
    rank_match_grades: Optional[list[RankMatchGrade]] = None
    rank_match_classes: Optional[list[RankMatchClass]] = None
    limited_title_screens: Optional[list[LimitedTitleScreen]] = None
    panel_mission_campaigns: Optional[list[PanelMissionCampaign]] = None
    event_missions: Optional[list[EventMission]] = None
    background_musics: Optional[list[BackgroundMusic]] = None
    offline_events: Optional[list[OfflineEvent]] = None
    another_3dmv_cut_ins: Optional[list[Another3dmvCutIn]] = None
    limited_time_musics: Optional[list[LimitedTimeMusic]] = None
    music_artists: Optional[list[MusicArtist]] = None
    beginner_mission_v2s: Optional[list[BeginnerMissionV2]] = None

    character_mission_v2_ex_jsons: Optional[list[CharacterMissionV2ExJson]] = None
    friend_invitation_campaigns: Optional[list[FriendInvitationCampaign]] = None
    unit_story_episode_groups: Optional[list[UnitStoryEpisodeGroup]] = None
    episode_background_musics: Optional[list[EpisodeBackgroundMusic]] = None
    virtual_item_relations: Optional[list[VirtualItemRelation]] = None
    virtual_live_cheer_message_relations: Optional[list[VirtualLiveCheerMessageRelation]] = None
    world_blooms: Optional[list[WorldBloom]] = None
    world_bloom_different_attribute_bonuses: Optional[list[WorldBloomDifferentAttributeBonus]] = None
    world_bloom_support_deck_bonuses: Optional[list[WorldBloomSupportDeckBonus]] = None
    world_bloom_chapter_ranking_reward_ranges: Optional[
        list[WorldBloomChapterRankingRewardRange]] = None

    card_extras: Optional[list[CardExtra]] = None
    sub_game_characters: Optional[list[SubGameCharacter]] = None
    character_archive_voices: Optional[list[CharacterArchiveVoice]] = None
    character_archive_voice_tags: Optional[list[CharacterArchiveVoiceTag]] = None
    live_clear_voices: Optional[list[LiveClearVoice]] = None
    ad_rewards: Optional[list[AdReward]] = None

    card_supplies: Optional[list[CardSupply]] = None
    card_supply_groups: Optional[list[CardSupplyGroup]] = None
    event_mission_selectable_rewards: Optional[list[EventMissionSelectableRewards]] = None
    area_spirit_world_trees: Optional[list[AreaSpiritWorldTree]] = None
    honor_mission_type_orders: Optional[list[HonorMissionTypeOrder]] = None
    gacha_bonus_item_receivable_rewards: Optional[list[GachaBonusItemReceivableReward]] = None
    gacha_bonus_reward_item_groups: Optional[list[Empty]] = None
    gacha_freebie_groups: Optional[list[GachaFreebieGroup]] = None
    home_exchange_buttons: Optional[list[HomeExchangeButton]] = None
    material_auto_exchange_music_vocals: Optional[list[MaterialAutoExchangeMusicVocal]] = None
    release_condition_logical_expressions: Optional[list[ReleaseConditionLogicalExpression]] = None
    action_set_lottery_conditions: Optional[list[ActionSetLotteryCondition]] = None
    story_missions: Optional[list[StoryMission]] = None

    costume3d_model_not_available_patterns: Optional[
        list[Costume3dModelPattern]
    ] = None
    costume3d_model_default_hairs: Optional[
        list[Costume3dModelPattern]
    ] = None