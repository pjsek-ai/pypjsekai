# SPDX-FileCopyrightText: 2022-present Erik Chan <erikchan002@gmail.com>
#
# SPDX-License-Identifier: MIT

from datetime import datetime
from typing import List, Optional, Union

from .model import ModelWithExtra
from pjsekai.enums import *


class GameCharacter(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    resourceId: Optional[int]
    firstName: Optional[str]
    givenName: Optional[str]
    firstNameRuby: Optional[str]
    givenNameRuby: Optional[str]
    gender: Optional[Union[Gender, Unknown]]
    height: Optional[float]
    live2dHeightAdjustment: Optional[float]
    figure: Optional[Union[Figure, Unknown]]
    breastSize: Optional[Union[BreastSize, Unknown]]
    modelName: Optional[str]
    unit: Optional[Union[Unit, Unknown]]
    supportUnitType: Optional[Union[SupportUnitType, Unknown]]


class GameCharacterUnit(ModelWithExtra):
    id: Optional[int]
    gameCharacterId: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    colorCode: Optional[str]
    skinColorCode: Optional[str]
    skinShadowColorCode1: Optional[str]
    skinShadowColorCode2: Optional[str]


class OutsideCharacter(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]


class Character3d(ModelWithExtra):
    id: Optional[int]
    characterType: Optional[Union[CharacterType, Unknown]]
    characterId: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    name: Optional[str]
    headCostume3dId: Optional[int]
    hairCostume3dId: Optional[int]
    bodyCostume3dId: Optional[int]


class Character2d(ModelWithExtra):
    id: Optional[int]
    characterType: Optional[Union[CharacterType, Unknown]]
    characterId: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    assetName: Optional[str]


class CharacterProfile(ModelWithExtra):
    characterId: Optional[int]
    characterVoice: Optional[str]
    birthday: Optional[str]
    height: Optional[str]
    school: Optional[str]
    schoolYear: Optional[str]
    hobby: Optional[str]
    specialSkill: Optional[str]
    favoriteFood: Optional[str]
    hatedFood: Optional[str]
    weak: Optional[str]
    introduction: Optional[str]
    scenarioId: Optional[str]


class Bond(ModelWithExtra):
    id: Optional[int]
    groupId: Optional[int]
    characterId1: Optional[int]
    characterId2: Optional[int]


class Live2d(ModelWithExtra):
    id: Optional[int]
    characterId: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    assetbundleName: Optional[str]
    motion: Optional[str]
    expression: Optional[str]
    weight: Optional[int]


class BondsLive2d(Live2d):
    defaultFlg: Optional[bool]


class BondsRankUpLive2d(Live2d):
    defaultFlg: Optional[bool]


class UnitProfile(ModelWithExtra):
    unit: Optional[Union[Unit, Unknown]]
    unitName: Optional[str]
    seq: Optional[int]
    profileSentence: Optional[str]
    colorCode: Optional[str]


class ActionSet(ModelWithExtra):
    id: Optional[int]
    areaId: Optional[int]
    scriptId: Optional[str]
    characterIds: Optional[List[int]]
    archiveDisplayType: Optional[Union[ArchiveDisplayType, Unknown]]
    archivePublishedAt: Optional[datetime]
    releaseConditionId: Optional[datetime]
    scenarioId: Optional[str]
    actionSetType: Optional[Union[ActionSetType, Unknown]]
    specialSeasonId: Optional[int]


class Area(ModelWithExtra):
    id: Optional[int]
    assetbundleName: Optional[str]
    areaType: Optional[Union[AreaType, Unknown]]
    viewType: Optional[Union[ViewType, Unknown]]
    name: Optional[str]
    releaseConditionId: Optional[int]
    label: Optional[str]
    startAt: Optional[datetime]
    endAt: Optional[datetime]


class AreaPlaylist(ModelWithExtra):
    id: Optional[int]
    areaId: Optional[int]
    musicId: Optional[int]
    assetbundleName: Optional[str]
    bgmName: Optional[str]
    releaseConditionId: Optional[int]


class MobCharacter(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    gender: Optional[Union[Gender, Unknown]]


class CharacterCostume(ModelWithExtra):
    id: Optional[int]
    characterId: Optional[int]
    costumeId: Optional[int]
    sdAssetbundleName: Optional[str]
    live2dAssetbundleName: Optional[str]


class CardCostume3d(ModelWithExtra):
    cardId: Optional[int]
    costume3dId: Optional[int]


class CardParameter(ModelWithExtra):
    id: Optional[int]
    cardId: Optional[int]
    cardLevel: Optional[int]
    cardParameterType: Optional[Union[CardParameterType, Unknown]]
    power: Optional[int]


class Cost(ModelWithExtra):
    resourceId: Optional[int]
    resourceType: Optional[Union[ResourceType, Unknown]]
    resourceLevel: Optional[int]
    quantity: Optional[int]


class SpecialTrainingCost(ModelWithExtra):
    cardId: Optional[int]
    seq: Optional[int]
    cost: Optional[Cost]


class MasterLessonAchieveResource(ModelWithExtra):
    releaseConditionId: Optional[int]
    cardId: Optional[int]
    masterRank: Optional[int]
    resources: Optional[List[Union[dict, str, int]]]


class Card(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    characterId: Optional[int]
    cardRarityType: Optional[Union[CardRarityType, Unknown]]
    specialTrainingPower1BonusFixed: Optional[int]
    specialTrainingPower2BonusFixed: Optional[int]
    specialTrainingPower3BonusFixed: Optional[int]
    attr: Optional[Union[CardAttr, Unknown]]
    supportunit: Optional[Union[Unit, Unknown]]
    skillId: Optional[int]
    cardSkillName: Optional[str]
    prefix: Optional[str]
    assetbundleName: Optional[str]
    gachaPhrase: Optional[str]
    flavorText: Optional[str]
    releaseAt: Optional[datetime]
    archivePublishedAt: Optional[datetime]
    cardParameters: Optional[List[CardParameter]]
    specialTrainingCosts: Optional[List[SpecialTrainingCost]]
    masterLessonAchieveResources: Optional[List[MasterLessonAchieveResource]]
    archiveDisplayType: Optional[Union[ArchiveDisplayType, Unknown]]


class SkillEffectDetail(ModelWithExtra):
    id: Optional[int]
    level: Optional[int]
    activateEffectDuration: Optional[float]
    activateEffectValueType: Optional[Union[ActivateEffectValueType, Unknown]]
    activateEffectValue: Optional[int]


class SkillEnhanceCondition(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    unit: Optional[Union[Unit, Unknown]]


class SkillEnhance(ModelWithExtra):
    id: Optional[int]
    skillEnhanceType: Optional[Union[SkillEnhanceType, Unknown]]
    activateEffectValueType: Optional[Union[ActivateEffectValueType, Unknown]]
    activateEffectValue: Optional[int]
    skillEnhanceCondition: Optional[SkillEnhanceCondition]


class SkillEffect(ModelWithExtra):
    id: Optional[int]
    skillEffectType: Optional[Union[SkillEffectType, Unknown]]
    activateNotesJudgmentType: Optional[Union[IngameNoteJudgeType, Unknown]]
    skillEffectDetails: Optional[List[SkillEffectDetail]]
    activateLife: Optional[int]
    conditionType: Optional[Union[SkillEffectConditionType, Unknown]]
    skillEnhance: Optional[SkillEnhance]


class Skill(ModelWithExtra):
    id: Optional[int]
    shortDescription: Optional[str]
    description: Optional[str]
    descriptionSpriteName: Optional[str]
    skillFilterId: Optional[int]
    skillEffects: Optional[List[SkillEffect]]


class CardEpisode(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    cardId: Optional[int]
    title: Optional[str]
    scenarioId: Optional[str]
    assetbundleName: Optional[str]
    releaseConditionId: Optional[int]
    power1BonusFixed: Optional[int]
    power2BonusFixed: Optional[int]
    power3BonusFixed: Optional[int]
    rewardResourceBoxIds: Optional[List[int]]
    costs: Optional[List[Cost]]
    cardEpisodePartType: Optional[Union[CardEpisodePartType, Unknown]]


class CardRarity(ModelWithExtra):
    cardRarityType: Optional[Union[CardRarityType, Unknown]]
    seq: Optional[int]
    maxLevel: Optional[int]
    maxSkillLevel: Optional[int]
    trainingMaxLevel: Optional[int]


class CardSkillCost(ModelWithExtra):
    id: Optional[int]
    materialId: Optional[int]
    exp: Optional[int]


class Music(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    releaseConditionId: Optional[int]
    categories: Optional[List[Union[MusicCategory, Unknown]]]
    title: Optional[str]
    pronunciation: Optional[str]
    lyricist: Optional[str]
    composer: Optional[str]
    arranger: Optional[str]
    dancerCount: Optional[int]
    selfDancerPosition: Optional[int]
    assetbundleName: Optional[str]
    liveTalkBackgroundAssetbundleName: Optional[str]
    publishedAt: Optional[datetime]
    liveStageId: Optional[int]
    fillerSec: Optional[float]
    musicCollaborationId: Optional[int]


class MusicTag(ModelWithExtra):
    id: Optional[int]
    musicId: Optional[int]
    musicTag: Optional[str]
    seq: Optional[int]


class MusicDifficulty(ModelWithExtra):
    id: Optional[int]
    musicId: Optional[int]
    musicDifficulty: Optional[Union[MusicDifficultyType, Unknown]]
    playLevel: Optional[int]
    releaseConditionId: Optional[int]
    noteCount: Optional[int]


class Character(ModelWithExtra):
    id: Optional[int]
    musicId: Optional[int]
    musicVocalId: Optional[int]
    characterType: Optional[Union[CharacterType, Unknown]]
    characterId: Optional[int]
    seq: Optional[int]


class MusicVocal(ModelWithExtra):
    id: Optional[int]
    musicId: Optional[int]
    musicVocalType: Optional[Union[MusicVocalType, Unknown]]
    seq: Optional[int]
    releaseConditionId: Optional[int]
    caption: Optional[str]
    characters: Optional[List[Character]]
    assetbundleName: Optional[str]
    archivePublishedAt: Optional[datetime]
    specialSeasonId: Optional[int]
    archiveDisplayType: Optional[Union[ArchiveDisplayType, Unknown]]


class MusicDanceMember(ModelWithExtra):
    id: Optional[int]
    musicId: Optional[int]
    defaultMusicType: Optional[Union[DefaultMusicType, Unknown]]
    characterId1: Optional[int]
    unit1: Optional[Union[Unit, Unknown]]
    characterId2: Optional[int]
    unit2: Optional[Union[Unit, Unknown]]
    characterId3: Optional[int]
    unit3: Optional[Union[Unit, Unknown]]
    characterId4: Optional[int]
    unit4: Optional[Union[Unit, Unknown]]
    characterId5: Optional[int]
    unit5: Optional[Union[Unit, Unknown]]


class MusicAchievement(ModelWithExtra):
    id: Optional[int]
    musicAchievementType: Optional[Union[MusicAchievementType, Unknown]]
    musicAchievementTypeValue: Optional[str]
    resourceBoxId: Optional[int]
    musicDifficultyType: Optional[Union[MusicDifficultyType, Unknown]]


class MusicVideoCharacter(ModelWithExtra):
    id: Optional[int]
    musicId: Optional[int]
    defaultMusicType: Optional[Union[DefaultMusicType, Unknown]]
    gameCharacterUnitId: Optional[int]
    dancePriority: Optional[int]
    seq: Optional[int]
    priority: Optional[int]


class MusicAssetVariant(ModelWithExtra):
    id: Optional[int]
    musicVocalId: Optional[int]
    seq: Optional[int]
    musicAssetType: Optional[Union[MusicAssetType, Unknown]]
    assetbundleName: Optional[str]


class MusicCollaboration(ModelWithExtra):
    id: Optional[int]
    label: Optional[str]


class EpisodeMusicVideoCostume(ModelWithExtra):
    id: Optional[int]
    musicVocalId: Optional[int]
    character3dId1: Optional[int]
    character3dId2: Optional[int]
    character3dId3: Optional[int]
    character3dId4: Optional[int]
    character3dId5: Optional[int]


class ReleaseCondition(ModelWithExtra):
    id: Optional[int]
    sentence: Optional[str]
    releaseConditionType: Optional[Union[ReleaseConditionType, Unknown]]
    releaseConditionTypeLevel: Optional[int]
    releaseConditionTypeId: Optional[int]
    releaseConditionTypeQuantity: Optional[int]


class PlayLevelScore(ModelWithExtra):
    liveType: Optional[Union[LiveType, Unknown]]
    playLevel: Optional[int]
    s: Optional[int]
    a: Optional[int]
    b: Optional[int]
    c: Optional[int]


class IngameCombo(ModelWithExtra):
    id: Optional[int]
    fromCount: Optional[int]
    toCount: Optional[int]
    scoreCoefficient: Optional[float]


class IngameNote(ModelWithExtra):
    id: Optional[int]
    ingameNoteType: Optional[Union[IngameNoteType, Unknown]]
    scoreCoefficient: Optional[float]
    damageBad: Optional[int]
    damageMiss: Optional[int]


class IngameNoteJudge(ModelWithExtra):
    id: Optional[int]
    ingameNoteJadgeType: Optional[Union[IngameNoteJudgeType, Unknown]]
    scoreCoefficient: Optional[float]
    damage: Optional[int]


class IngamePlayLevel(ModelWithExtra):
    playLevel: Optional[int]
    scoreCoefficient: Optional[float]


class IngameCutin(ModelWithExtra):
    id: Optional[int]
    musicDifficulty: Optional[Union[MusicDifficultyType, Unknown]]
    combo: Optional[int]


class IngameCutinCharacter(ModelWithExtra):
    id: Optional[int]
    ingameCutinCharacterType: Optional[Union[IngameCutinCharacterType, Unknown]]
    priority: Optional[int]
    gameCharacterUnitId1: Optional[int]
    gameCharacterUnitId2: Optional[int]
    assetbundleName1: Optional[str]
    assetbundleName2: Optional[str]
    releaseConditionId: Optional[int]


class IngameJudgeFrame(ModelWithExtra):
    id: Optional[int]
    ingameNoteType: Optional[Union[IngameNoteType, Unknown]]
    perfect: Optional[float]
    great: Optional[float]
    good: Optional[float]
    bad: Optional[float]
    perfectBefore: Optional[float]
    perfectAfter: Optional[float]
    greatBefore: Optional[float]
    greatAfter: Optional[float]
    goodBefore: Optional[float]
    goodAfter: Optional[float]
    badBefore: Optional[float]
    badAfter: Optional[float]


class IngameNoteJudgeTechnicalScore(ModelWithExtra):
    id: Optional[int]
    liveType: Optional[Union[LiveType, Unknown]]
    ingameNoteJadgeType: Optional[Union[IngameNoteJudgeType, Unknown]]
    score: Optional[int]


class Shop(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    shopType: Optional[Union[ShopType, Unknown]]
    areaId: Optional[int]
    name: Optional[str]
    releaseConditionId: Optional[int]


class ShopItemCost(ModelWithExtra):
    shopItemId: Optional[int]
    seq: Optional[int]
    cost: Optional[Cost]


class ShopItem(ModelWithExtra):
    id: Optional[int]
    shopId: Optional[int]
    seq: Optional[int]
    releaseConditionId: Optional[int]
    resourceBoxId: Optional[int]
    costs: Optional[List[ShopItemCost]]
    startAt: Optional[datetime]


class Costume3dShopItemCost(Cost):
    id: Optional[int]
    costume3dShopItemId: Optional[int]
    seq: Optional[int]


class Costume3dShopItem(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    groupId: Optional[int]
    name: Optional[str]
    bodyCostume3dId: Optional[int]
    releaseConditionId: Optional[int]
    costs: Optional[List[Costume3dShopItemCost]]
    startAt: Optional[datetime]
    headCostume3dId: Optional[int]


class AreaItem(ModelWithExtra):
    id: Optional[int]
    areaId: Optional[int]
    name: Optional[str]
    flavorText: Optional[str]
    spawnPoint: Optional[str]
    assetbundleName: Optional[str]


class AreaItemLevel(ModelWithExtra):
    areaItemId: Optional[int]
    level: Optional[int]
    targetunit: Optional[Union[Unit, Unknown]]
    targetCardAttr: Optional[Union[CardAttr, Unknown]]
    targetGameCharacterId: Optional[int]
    power1BonusRate: Optional[float]
    power1AllMatchBonusRate: Optional[float]
    power2BonusRate: Optional[float]
    power2AllMatchBonusRate: Optional[float]
    power3BonusRate: Optional[float]
    power3AllMatchBonusRate: Optional[float]
    sentence: Optional[str]


class Material(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    flavorText: Optional[str]
    materialType: Optional[Union[MaterialType, Unknown]]


class GachaCardRarityRate(ModelWithExtra):
    id: Optional[int]
    groupId: Optional[int]
    cardRarityType: Optional[Union[CardRarityType, Unknown]]
    lotteryType: Optional[Union[LotteryType, Unknown]]
    rate: Optional[float]


class GachaDetail(ModelWithExtra):
    id: Optional[int]
    gachaId: Optional[int]
    cardId: Optional[int]
    weight: Optional[int]
    isWish: Optional[bool]


class GachaBehavior(ModelWithExtra):
    id: Optional[int]
    gachaId: Optional[int]
    groupId: Optional[int]
    priority: Optional[int]
    gachaBehaviorType: Optional[Union[GachaBehaviorType, Unknown]]
    costResourceType: Optional[Union[ResourceType, Unknown]]
    costResourceQuantity: Optional[int]
    spinCount: Optional[int]
    executeLimit: Optional[int]
    costResourceId: Optional[int]
    gachaExtraId: Optional[int]


class GachaPickup(ModelWithExtra):
    id: Optional[int]
    gachaId: Optional[int]
    cardId: Optional[int]
    gachaPickupType: Optional[Union[GachaPickupType, Unknown]]


class GachaInformation(ModelWithExtra):
    gachaId: Optional[int]
    summary: Optional[str]
    description: Optional[str]


class Gacha(ModelWithExtra):
    id: Optional[int]
    gachaType: Optional[Union[GachaType, Unknown]]
    name: Optional[str]
    seq: Optional[int]
    assetbundleName: Optional[str]
    gachaCardRarityRateGroupId: Optional[int]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    isShowPeriod: Optional[bool]
    gachaCeilItemId: Optional[int]
    wishSelectCount: Optional[int]
    wishFixedSelectCount: Optional[int]
    wishLimitedSelectCount: Optional[int]
    gachaCardRarityRates: Optional[List[GachaCardRarityRate]]
    gachaDetails: Optional[List[GachaDetail]]
    gachaBehaviors: Optional[List[GachaBehavior]]
    gachaPickups: Optional[List[GachaPickup]]
    gachaPickupCostumes: Optional[List[Union[dict, str, int]]]
    gachaInformation: Optional[GachaInformation]
    drawableGachaHour: Optional[int]
    gachaBonusId: Optional[int]
    spinLimit: Optional[int]


class GachaBonus(ModelWithExtra):
    id: Optional[int]


class GachaBonusPoint(ModelWithExtra):
    id: Optional[int]
    resourceType: Optional[Union[ResourceType, Unknown]]
    point: Optional[float]


class GachaExtra(ModelWithExtra):
    id: Optional[int]
    resourceBoxId: Optional[int]


class GiftGachaExchange(ModelWithExtra):
    id: Optional[int]
    gachaId: Optional[int]
    seq: Optional[int]
    resourceBoxId: Optional[int]


class PracticeTicket(ModelWithExtra):
    id: Optional[int]
    name: Optional[str]
    exp: Optional[int]
    flavorText: Optional[str]


class SkillPracticeTicket(PracticeTicket):
    pass


class Level(ModelWithExtra):
    id: Optional[int]
    levelType: Optional[Union[LevelType, Unknown]]
    level: Optional[int]
    totalExp: Optional[int]


class Episode(ModelWithExtra):
    id: Optional[int]
    episodeNo: Optional[int]
    title: Optional[str]
    assetbundleName: Optional[str]
    scenarioId: Optional[str]
    releaseConditionId: Optional[int]
    rewardResourceBoxIds: Optional[List[int]]


class UnitStoryEpisode(Episode):
    unit: Optional[Union[Unit, Unknown]]
    chapterNo: Optional[int]
    unitEpisodeCategory: Optional[Union[Unit, Unknown]]
    episodeNoLabel: Optional[str]
    limitedReleaseStartAt: Optional[datetime]
    limitedReleaseEndAt: Optional[datetime]
    andReleaseConditionId: Optional[int]


class Chapter(ModelWithExtra):
    id: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    chapterNo: Optional[int]
    title: Optional[str]
    assetbundleName: Optional[str]
    episodes: Optional[List[UnitStoryEpisode]]


class UnitStory(ModelWithExtra):
    unit: Optional[Union[Unit, Unknown]]
    seq: Optional[int]
    assetbundleName: Optional[str]
    chapters: Optional[List[Chapter]]


class SpecialStoryEpisode(Episode):
    specialStoryId: Optional[int]
    specialStoryEpisodeType: Optional[str]
    isAbleSkip: Optional[bool]
    isActionSetRefresh: Optional[bool]
    specialStoryEpisodeTypeId: Optional[int]


class SpecialStory(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    title: Optional[str]
    assetbundleName: Optional[str]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    episodes: Optional[List[SpecialStoryEpisode]]


class Config(ModelWithExtra):
    configKey: Optional[str]
    value: Optional[str]


class ClientConfig(ModelWithExtra):
    id: Optional[int]
    value: Optional[str]
    type: Optional[Union[ClientConfigType, Unknown]]


class Wording(ModelWithExtra):
    wordingKey: Optional[str]
    value: Optional[str]


class Costume3d(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    costume3dGroupId: Optional[int]
    costume3dType: Optional[Union[Costume3dType, Unknown]]
    name: Optional[str]
    partType: Optional[Union[PartType, Unknown]]
    colorId: Optional[int]
    colorName: Optional[str]
    characterId: Optional[int]
    costume3dRarity: Optional[Union[Costume3dRarity, Unknown]]
    howToObtain: Optional[str]
    assetbundleName: Optional[str]
    designer: Optional[str]
    archiveDisplayType: Optional[Union[ArchiveDisplayType, Unknown]]
    archivePublishedAt: Optional[datetime]
    publishedAt: Optional[datetime]


class Costume3dModel(ModelWithExtra):
    id: Optional[int]
    costume3dId: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    headCostume3dAssetbundleType: Optional[Union[HeadCostume3dAssetbundleType, Unknown]]
    thumbnailAssetbundleName: Optional[str]
    assetbundleName: Optional[str]
    colorAssetbundleName: Optional[str]
    part: Optional[str]


class Costume3dModelAvailablePattern(ModelWithExtra):
    id: Optional[int]
    headCostume3dId: Optional[int]
    hairCostume3dId: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    isDefault: Optional[bool]


class GameCharacterUnit3dMotion(ModelWithExtra):
    id: Optional[int]
    gameCharacterUnitId: Optional[int]
    motionType: Optional[Union[MotionType, Unknown]]
    assetbundleName: Optional[str]


class Costume2d(ModelWithExtra):
    id: Optional[int]
    costume2dGroupId: Optional[int]
    character2dId: Optional[int]
    fromMmddhh: Optional[str]
    toMmddhh: Optional[str]
    live2dAssetbundleName: Optional[str]
    spineAssetbundleName: Optional[str]


class Costume2dGroup(ModelWithExtra):
    id: Optional[int]
    name: Optional[str]


class Topic(ModelWithExtra):
    id: Optional[int]
    topicType: Optional[Union[TopicType, Unknown]]
    topicTypeId: Optional[int]
    releaseConditionId: Optional[int]


class LiveStage(ModelWithExtra):
    id: Optional[int]
    name: Optional[str]
    assetbundleName: Optional[str]


class Stamp(ModelWithExtra):
    id: Optional[int]
    stampType: Optional[Union[StampType, Unknown]]
    seq: Optional[int]
    name: Optional[str]
    assetbundleName: Optional[str]
    balloonAssetbundleName: Optional[str]
    characterId1: Optional[int]
    gameCharacterUnitId: Optional[int]
    archivePublishedAt: Optional[datetime]
    description: Optional[str]
    archiveDisplayType: Optional[Union[ArchiveDisplayType, Unknown]]


class MultiLiveLobby(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    photonLobbyName: Optional[str]
    matchingLogic: Optional[Union[MatchingLogic, Unknown]]
    totalPower: Optional[int]
    assetbundleName: Optional[str]
    multiLiveLobbyType: Optional[Union[MultiLiveLobbyType, Unknown]]


class MasterLessonCost(Cost):
    id: Optional[int]
    cardRarityType: Optional[Union[CardRarityType, Unknown]]
    masterRank: Optional[int]
    seq: Optional[int]


class MasterLesson(ModelWithExtra):
    cardRarityType: Optional[Union[CardRarityType, Unknown]]
    masterRank: Optional[int]
    power1BonusFixed: Optional[int]
    power2BonusFixed: Optional[int]
    power3BonusFixed: Optional[int]
    characterRankExp: Optional[int]
    costs: Optional[List[MasterLessonCost]]
    rewards: Optional[List[Union[dict, str, int]]]


class MasterLessonReward(ModelWithExtra):
    id: Optional[int]
    cardId: Optional[int]
    masterRank: Optional[int]
    seq: Optional[int]
    resourceBoxId: Optional[int]
    cardRarity: Optional[int]


class CardExchangeResource(ModelWithExtra):
    cardRarityType: Optional[Union[CardRarityType, Unknown]]
    seq: Optional[int]
    resourceBoxId: Optional[int]


class MaterialExchangeCost(Cost):
    materialExchangeId: Optional[int]
    costGroupId: Optional[int]
    seq: Optional[int]


class MaterialExchange(ModelWithExtra):
    id: Optional[int]
    materialExchangeSummaryId: Optional[int]
    seq: Optional[int]
    resourceBoxId: Optional[int]
    refreshCycle: Optional[Union[RefreshCycle, Unknown]]
    costs: Optional[List[MaterialExchangeCost]]
    exchangeLimit: Optional[int]
    startAt: Optional[datetime]


class MaterialExchangeSummary(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    exchangeCategory: Optional[Union[ExchangeCategory, Unknown]]
    materialExchangeType: Optional[Union[MaterialExchangeType, Unknown]]
    name: Optional[str]
    assetbundleName: Optional[str]
    startAt: Optional[datetime]
    materialExchanges: Optional[List[MaterialExchange]]
    endAt: Optional[datetime]
    notificationRemainHour: Optional[int]


class BoostItem(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    recoveryValue: Optional[int]
    assetBundleName: Optional[str]
    flavorText: Optional[str]


class BillingProduct(ModelWithExtra):
    id: Optional[int]
    groupId: Optional[int]
    platform: Optional[Platform]
    productId: Optional[str]
    price: Optional[int]
    unitPrice: Optional[float]


class BillingShopItem(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    billingShopItemType: Optional[Union[BillingShopItemType, Unknown]]
    billingProductGroupId: Optional[int]
    name: Optional[str]
    description: Optional[str]
    billableLimitType: Optional[Union[BillableLimitType, Unknown]]
    billableLimitResetIntervalType: Optional[Union[BillableLimitResetIntervalType, Unknown]]
    assetbundleName: Optional[str]
    resourceBoxId: Optional[int]
    billableLimitValue: Optional[int]
    bonusResourceBoxId: Optional[int]
    label: Optional[str]
    endAt: Optional[datetime]
    startAt: Optional[datetime]
    billableLimitResetIntervalValue: Optional[int]
    purchaseOption: Optional[Union[PurchaseOption, Unknown]]


class BillingShopItemExchangeCost(Cost):
    id: Optional[int]
    billingShopItemId: Optional[int]


class ColorfulPass(ModelWithExtra):
    id: Optional[int]
    resourceBoxId: Optional[int]
    receivableDays: Optional[int]
    presentSentence: Optional[str]
    expireDays: Optional[int]
    dailyPaidGachaSpinLimit: Optional[int]
    challengeLivePointMultiple: Optional[int]
    livePointMultiple: Optional[int]


class JewelBehavior(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    jewelBehaviorType: Optional[Union[JewelBehaviorType, Unknown]]
    jewelBehaviorTypeQuantity: Optional[int]
    amount: Optional[int]


class CharacterRankAchieveResource(ModelWithExtra):
    releaseConditionId: Optional[int]
    characterId: Optional[int]
    characterRank: Optional[int]
    resources: Optional[List[Union[dict, str, int]]]


class CharacterRank(ModelWithExtra):
    id: Optional[int]
    characterId: Optional[int]
    characterRank: Optional[int]
    power1BonusRate: Optional[float]
    power2BonusRate: Optional[float]
    power3BonusRate: Optional[float]
    rewardResourceBoxIds: Optional[List[int]]
    characterRankAchieveResources: Optional[List[CharacterRankAchieveResource]]


class CharacterMissionV2(ModelWithExtra):
    id: Optional[int]
    characterMissionType: Optional[Union[CharacterMissionType, Unknown]]
    characterId: Optional[int]
    parameterGroupId: Optional[int]
    sentence: Optional[str]
    progressSentence: Optional[str]
    isAchievementMission: Optional[bool]


class CharacterMissionV2ParameterGroup(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    requirement: Optional[int]
    exp: Optional[int]


class CharacterMissionV2AreaItem(ModelWithExtra):
    id: Optional[int]
    characterMissionType: Optional[Union[CharacterMissionType, Unknown]]
    areaItemId: Optional[int]
    characterId: Optional[int]
    unit: Optional[Union[Unit, Unknown]]


class SystemLive2d(Live2d):
    serif: Optional[str]
    voice: Optional[str]
    publishedAt: Optional[datetime]
    closedAt: Optional[datetime]
    specialSeasonId: Optional[int]


class Reward(ModelWithExtra):
    id: Optional[int]
    missionType: Optional[Union[MissionType, Unknown]]
    missionId: Optional[int]
    seq: Optional[int]
    resourceBoxId: Optional[int]


class NormalMission(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    normalMissionType: Optional[Union[NormalMissionType, Unknown]]
    requirement: Optional[int]
    sentence: Optional[str]
    rewards: Optional[List[Reward]]


class BeginnerMission(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    beginnerMissionType: Optional[Union[BeginnerMissionType, Unknown]]
    beginnerMissionCategory: Optional[Union[BeginnerMissionCategory, Unknown]]
    requirement: Optional[int]
    sentence: Optional[str]
    rewards: Optional[List[Reward]]


class Detail(ModelWithExtra):
    resourceBoxPurpose: Optional[Union[ResourceBoxPurpose, Unknown]]
    resourceBoxId: Optional[int]
    seq: Optional[int]
    resourceType: Optional[Union[ResourceType, Unknown]]
    resourceQuantity: Optional[int]
    resourceId: Optional[int]
    resourceLevel: Optional[int]


class ResourceBox(ModelWithExtra):
    resourceBoxPurpose: Optional[Union[ResourceBoxPurpose, Unknown]]
    id: Optional[int]
    resourceBoxType: Optional[Union[ResourceBoxType, Unknown]]
    details: Optional[List[Detail]]
    description: Optional[str]
    name: Optional[str]
    assetbundleName: Optional[str]


class LiveMissionPeriod(ModelWithExtra):
    id: Optional[int]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    sentence: Optional[str]


class LiveMission(ModelWithExtra):
    id: Optional[int]
    liveMissionPeriodId: Optional[int]
    liveMissionType: Optional[Union[LiveMissionType, Unknown]]
    requirement: Optional[int]
    rewards: Optional[List[Reward]]


class LiveMissionPass(ModelWithExtra):
    id: Optional[int]
    liveMissionPeriodId: Optional[int]
    costumeName: Optional[str]
    character3dId1: Optional[int]
    character3dId2: Optional[int]
    maleAssetbundleName: Optional[str]
    femaleAssetbundleName: Optional[str]


class PenlightColor(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    description: Optional[str]
    colorCode: Optional[str]
    characterId: Optional[int]
    unit: Optional[Union[Unit, Unknown]]


class Penlight(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    defaultPenlightColorId: Optional[int]
    assetbundleName: Optional[str]


class LiveTalk(ModelWithExtra):
    id: Optional[int]
    liveTalkType: Optional[Union[LiveTalkType, Unknown]]
    scenarioId: Optional[str]
    characterId1: Optional[int]
    characterId2: Optional[int]


class Tip(ModelWithExtra):
    id: Optional[int]
    title: Optional[str]
    description: Optional[str]
    fromUserRank: Optional[int]
    toUserRank: Optional[int]
    assetbundleName: Optional[str]


class GachaCeilItem(ModelWithExtra):
    id: Optional[int]
    gachaId: Optional[int]
    name: Optional[str]
    assetbundleName: Optional[str]
    convertStartAt: Optional[datetime]
    convertResourceBoxId: Optional[int]


class GachaCeilExchangeCost(Cost):
    gachaCeilExchangeId: Optional[int]
    gachaCeilItemId: Optional[int]


class GachaCeilExchangeSubstituteCost(Cost):
    id: Optional[int]
    substituteQuantity: Optional[int]


class GachaCeilExchange(ModelWithExtra):
    id: Optional[int]
    gachaCeilExchangeSummaryId: Optional[int]
    seq: Optional[int]
    resourceBoxId: Optional[int]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    gachaCeilExchangeCost: Optional[GachaCeilExchangeCost]
    gachaCeilExchangeSubstituteCosts: Optional[List[GachaCeilExchangeSubstituteCost]]
    exchangeLimit: Optional[int]
    gachaCeilExchangeLabelType: Optional[Union[GachaCeilExchangeLabelType, Unknown]]
    substituteLimit: Optional[int]


class GachaCeilExchangeSummary(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    gachaId: Optional[int]
    assetbundleName: Optional[str]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    gachaCeilExchanges: Optional[List[GachaCeilExchange]]
    gachaCeilItemId: Optional[int]


class PlayerRankReward(ModelWithExtra):
    id: Optional[int]
    playerRank: Optional[int]
    seq: Optional[int]
    resourceBoxId: Optional[int]


class GachaTicket(ModelWithExtra):
    id: Optional[int]
    name: Optional[str]
    assetbundleName: Optional[str]


class HonorGroup(ModelWithExtra):
    id: Optional[int]
    name: Optional[str]
    honorType: Optional[Union[HonorType, Unknown]]
    archivePublishedAt: Optional[datetime]
    backgroundAssetbundleName: Optional[str]


class HonorLevel(ModelWithExtra):
    honorId: Optional[int]
    level: Optional[int]
    bonus: Optional[int]
    description: Optional[str]


class Honor(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    groupId: Optional[int]
    honorRarity: Optional[Union[HonorRarity, Unknown]]
    name: Optional[str]
    assetbundleName: Optional[str]
    levels: Optional[List[HonorLevel]]
    honorTypeId: Optional[int]


class HonorMission(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    honorMissionType: Optional[Union[HonorMissionType, Unknown]]
    requirement: Optional[int]
    sentence: Optional[str]
    rewards: Optional[List[Reward]]


class BondsHonorLevel(ModelWithExtra):
    id: Optional[int]
    bondsHonorId: Optional[int]
    level: Optional[int]
    description: Optional[str]


class BondsHonor(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    bondsGroupId: Optional[int]
    gameCharacterUnitId1: Optional[int]
    gameCharacterUnitId2: Optional[int]
    honorRarity: Optional[Union[HonorRarity, Unknown]]
    name: Optional[str]
    description: Optional[str]
    levels: Optional[List[BondsHonorLevel]]
    configurableUnitVirtualSinger: Optional[bool]


class BondsHonorWord(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    bondsGroupId: Optional[int]
    assetbundleName: Optional[str]
    name: Optional[str]
    description: Optional[str]


class BondsReward(ModelWithExtra):
    id: Optional[int]
    bondsGroupId: Optional[int]
    rank: Optional[int]
    seq: Optional[int]
    bondsRewardType: Optional[Union[BondsRewardType, Unknown]]
    resourceBoxId: Optional[int]
    description: Optional[str]


class ChallengeLiveDetail(ModelWithExtra):
    id: Optional[int]
    challengeLiveId: Optional[int]
    challengeLiveType: Optional[Union[LiveType, Unknown]]


class ChallengeLive(ModelWithExtra):
    id: Optional[int]
    playableCount: Optional[int]
    challengeLiveDetails: Optional[List[ChallengeLiveDetail]]


class ChallengeLiveDeck(ModelWithExtra):
    id: Optional[int]
    characterId: Optional[int]
    releaseConditionId: Optional[int]
    cardLimit: Optional[int]


class ChallengeLiveStage(ModelWithExtra):
    id: Optional[int]
    characterId: Optional[int]
    rank: Optional[int]
    name: Optional[str]
    nextStageChallengePoint: Optional[int]
    completeStageResourceBoxId: Optional[int]
    completeStageCharacterExp: Optional[int]


class ChallengeLiveStageEx(ModelWithExtra):
    id: Optional[int]
    characterId: Optional[int]
    fromRank: Optional[int]
    toRank: Optional[int]
    name: Optional[str]
    nextStageChallengePoint: Optional[int]
    completeStageResourceBoxId: Optional[int]
    completeStageCharacterExp: Optional[int]


class ChallengeLiveHighScoreReward(ModelWithExtra):
    id: Optional[int]
    characterId: Optional[int]
    highScore: Optional[int]
    resourceBoxId: Optional[int]


class ChallengeLiveCharacter(ModelWithExtra):
    id: Optional[int]
    characterId: Optional[int]
    releaseConditionId: Optional[int]
    orReleaseConditionId: Optional[int]


class ChallengeLivePlayDayReward(ModelWithExtra):
    id: Optional[int]
    challengeLivePlayDayRewardPeriodId: Optional[int]
    playDays: Optional[int]
    seq: Optional[int]
    resourceBoxId: Optional[int]


class ChallengeLivePlayDayRewardPeriod(ModelWithExtra):
    id: Optional[int]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    priority: Optional[int]
    challengeLivePlayDayRewards: Optional[List[ChallengeLivePlayDayReward]]


class VirtualLiveSetlist(ModelWithExtra):
    id: Optional[int]
    virtualLiveId: Optional[int]
    seq: Optional[int]
    virtualLiveSetlistType: Optional[Union[VirtualLiveSetlistType, Unknown]]
    assetbundleName: Optional[str]
    virtualLiveStageId: Optional[int]
    musicId: Optional[int]
    musicVocalId: Optional[int]
    character3dId1: Optional[int]
    character3dId2: Optional[int]
    character3dId3: Optional[int]
    character3dId4: Optional[int]
    character3dId5: Optional[int]
    character3dId6: Optional[int]


class VirtualLiveBeginnerSchedule(ModelWithExtra):
    id: Optional[int]
    virtualLiveId: Optional[int]
    dayOfWeek: Optional[Union[DayOfWeek, Unknown]]
    startTime: Optional[str]
    endTime: Optional[str]


class VirtualLiveSchedule(ModelWithExtra):
    id: Optional[int]
    virtualLiveId: Optional[int]
    seq: Optional[int]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    noticeGroupId: Optional[str]


class VirtualLiveCharacter(ModelWithExtra):
    id: Optional[int]
    virtualLiveId: Optional[int]
    gameCharacterUnitId: Optional[int]
    seq: Optional[int]


class VirtualLiveReward(ModelWithExtra):
    id: Optional[int]
    virtualLiveType: Optional[Union[VirtualLiveType, Unknown]]
    virtualLiveId: Optional[int]
    resourceBoxId: Optional[int]


class VirtualLiveWaitingRoom(ModelWithExtra):
    id: Optional[int]
    virtualLiveId: Optional[int]
    assetbundleName: Optional[str]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    lobbyAssetbundleName: Optional[str]


class VirtualItem(ModelWithExtra):
    id: Optional[int]
    virtualItemCategory: Optional[Union[VirtualItemCategory, Unknown]]
    seq: Optional[int]
    priority: Optional[int]
    name: Optional[str]
    assetbundleName: Optional[str]
    costVirtualCoin: Optional[int]
    costJewel: Optional[int]
    cheerPoint: Optional[int]
    effectAssetbundleName: Optional[str]
    effectExpressionType: Optional[Union[EffectExpressionType, Unknown]]
    unit: Optional[Union[Unit, Unknown]]
    gameCharacterUnitId: Optional[int]
    virtualItemLabelType: Optional[Union[VirtualItemLabelType, Unknown]]


class VirtualLiveAppeal(ModelWithExtra):
    id: Optional[int]
    virtualLiveId: Optional[int]
    virtualLiveStageStatus: Optional[Union[VirtualLiveStageStatus, Unknown]]
    appealText: Optional[str]


class VirtualLiveInformation(ModelWithExtra):
    virtualLiveId: Optional[int]
    summary: Optional[str]
    description: Optional[str]


class VirtualLive(ModelWithExtra):
    id: Optional[int]
    virtualLiveType: Optional[Union[VirtualLiveType, Unknown]]
    virtualLivePlatform: Optional[str]
    seq: Optional[int]
    name: Optional[str]
    assetbundleName: Optional[str]
    screenMvMusicVocalId: Optional[int]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    rankingAnnounceAt: Optional[datetime]
    virtualLiveSetlists: Optional[List[VirtualLiveSetlist]]
    virtualLiveBeginnerSchedules: Optional[List[VirtualLiveBeginnerSchedule]]
    virtualLiveSchedules: Optional[List[VirtualLiveSchedule]]
    virtualLiveCharacters: Optional[List[VirtualLiveCharacter]]
    virtualLiveReward: Optional[VirtualLiveReward]
    virtualLiveRewards: Optional[List[VirtualLiveReward]]
    virtualLiveCheerPointRewards: Optional[List[Union[dict, str, int]]]
    virtualLiveWaitingRoom: Optional[VirtualLiveWaitingRoom]
    virtualItems: Optional[List[VirtualItem]]
    virtualLiveAppeals: Optional[List[VirtualLiveAppeal]]
    virtualLiveInformation: Optional[VirtualLiveInformation]
    archiveReleaseConditionId: Optional[int]
    virtualLiveTicketId: Optional[int]


class VirtualShopItem(ModelWithExtra):
    id: Optional[int]
    virtualShopId: Optional[int]
    virtualShopItemType: Optional[Union[VirtualShopItemType, Unknown]]
    seq: Optional[int]
    resourceBoxId: Optional[int]
    costVirtualCoin: Optional[int]
    costJewel: Optional[int]
    startAt: Optional[datetime]
    costPaidJewel: Optional[int]
    endAt: Optional[datetime]
    limitValue: Optional[int]


class VirtualShop(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    virtualShopItems: Optional[List[VirtualShopItem]]
    virtualShopType: Optional[Union[VirtualShopType, Unknown]]
    virtualLiveId: Optional[int]


class VirtualLiveCheerMessage(ModelWithExtra):
    id: Optional[int]
    virtualLiveType: Optional[Union[VirtualLiveType, Unknown]]
    resourceType: Optional[Union[ResourceType, Unknown]]
    fromCostVirtualCoin: Optional[int]
    toCostVirtualCoin: Optional[int]
    fromCost: Optional[int]
    toCost: Optional[int]
    assetbundleName: Optional[str]
    messageLengthLimit: Optional[int]
    displaySec: Optional[float]
    messageSize: Optional[str]
    colorCode: Optional[str]
    virtualLiveCheerMessageDisplayLimitId: Optional[int]


class VirtualLiveCheerMessageDisplayLimit(ModelWithExtra):
    id: Optional[int]
    displayLimit: Optional[int]


class VirtualLiveTicket(ModelWithExtra):
    id: Optional[int]
    virtualLiveId: Optional[int]
    virtualLiveTicketType: Optional[Union[VirtualLiveTicketType, Unknown]]
    name: Optional[str]
    flavorText: Optional[str]
    assetbundleName: Optional[str]


class VirtualLivePamphlet(ModelWithExtra):
    id: Optional[int]
    virtualLiveId: Optional[int]
    name: Optional[str]
    flavorText: Optional[str]
    assetbundleName: Optional[str]


class AvatarAccessory(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    part: Optional[Union[AccessoryPart, Unknown]]
    assetbundleName: Optional[str]


class AvatarCostume(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    assetbundleName: Optional[str]


class AvatarMotion(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    syncMusicFlg: Optional[bool]
    repeatCount: Optional[int]
    assetbundleName: Optional[str]


class AvatarSkinColor(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    colorCode: Optional[str]


class AvatarCoordinate(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    assetbundleName: Optional[str]
    skinColorCode: Optional[str]
    costumeAssetbundleName: Optional[str]
    accessoryPart: Optional[Union[AccessoryPart, Unknown]]
    accessoryAssetbundleName: Optional[str]


class NgWord(ModelWithExtra):
    id: Optional[int]
    word: Optional[str]


class RuleSlide(ModelWithExtra):
    id: Optional[int]
    ruleSlideType: Optional[Union[RuleSlideType, Unknown]]
    assetbundleName: Optional[str]


class Facility(ModelWithExtra):
    id: Optional[int]
    facilityType: Optional[Union[FacilityType, Unknown]]
    releaseConditionId: Optional[int]
    andReleaseConditionId: Optional[int]


class OneTimeBehavior(ModelWithExtra):
    id: Optional[int]
    oneTimeBehaviorType: Optional[Union[OneTimeBehaviorType, Unknown]]
    releaseConditionId: Optional[int]


class LoginBonus(ModelWithExtra):
    id: Optional[int]
    day: Optional[int]
    resourceBoxId: Optional[int]


class BeginnerLoginBonus(ModelWithExtra):
    id: Optional[int]
    day: Optional[int]
    resourceBoxId: Optional[int]
    loginBonusId: Optional[int]


class BeginnerLoginBonusSummary(ModelWithExtra):
    id: Optional[int]
    loginBonusId: Optional[int]
    startAt: Optional[datetime]
    endAt: Optional[datetime]


class LimitedLoginBonusDetail(ModelWithExtra):
    id: Optional[int]
    limitedLoginBonusId: Optional[int]
    day: Optional[int]
    resourceBoxId: Optional[int]


class LimitedLoginBonus(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    assetbundleName: Optional[str]
    closeAt: Optional[datetime]
    limitedLoginBonusDetails: Optional[List[LimitedLoginBonusDetail]]


class LoginBonusLive2d(Live2d):
    serif: Optional[str]
    voice: Optional[str]
    publishedAt: Optional[datetime]
    closedAt: Optional[datetime]


class EventRankingReward(ModelWithExtra):
    id: Optional[int]
    eventRankingRewardRangeId: Optional[int]
    resourceBoxId: Optional[int]


class EventRankingRewardRange(ModelWithExtra):
    id: Optional[int]
    eventId: Optional[int]
    fromRank: Optional[int]
    toRank: Optional[int]
    eventRankingRewards: Optional[List[EventRankingReward]]


class Event(ModelWithExtra):
    id: Optional[int]
    eventType: Optional[Union[EventType, Unknown]]
    name: Optional[str]
    assetbundleName: Optional[str]
    bgmAssetbundleName: Optional[str]
    startAt: Optional[datetime]
    aggregateAt: Optional[datetime]
    rankingAnnounceAt: Optional[datetime]
    distributionStartAt: Optional[datetime]
    closedAt: Optional[datetime]
    distributionEndAt: Optional[datetime]
    virtualLiveId: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    eventRankingRewardRanges: Optional[List[EventRankingRewardRange]]
    eventPointAssetbundleName: Optional[str]


class EventMusic(ModelWithExtra):
    eventId: Optional[int]
    musicId: Optional[int]
    seq: Optional[int]
    releaseConditionId: Optional[int]


class EventDeckBonus(ModelWithExtra):
    id: Optional[int]
    eventId: Optional[int]
    gameCharacterUnitId: Optional[int]
    cardAttr: Optional[Union[CardAttr, Unknown]]
    bonusRate: Optional[float]


class EventRarityBonusRate(ModelWithExtra):
    id: Optional[int]
    cardRarityType: Optional[Union[CardRarityType, Unknown]]
    masterRank: Optional[int]
    bonusRate: Optional[float]


class EventItem(ModelWithExtra):
    id: Optional[int]
    eventId: Optional[int]
    name: Optional[str]
    flavorText: Optional[str]
    assetbundleName: Optional[str]


class EpisodeReward(ModelWithExtra):
    storyType: Optional[Union[StoryType, Unknown]]
    resourceBoxId: Optional[int]


class EventStoryEpisode(ModelWithExtra):
    id: Optional[int]
    eventStoryId: Optional[int]
    episodeNo: Optional[int]
    title: Optional[str]
    assetbundleName: Optional[str]
    scenarioId: Optional[str]
    releaseConditionId: Optional[int]
    episodeRewards: Optional[List[EpisodeReward]]


class EventStory(ModelWithExtra):
    id: Optional[int]
    eventId: Optional[int]
    assetbundleName: Optional[str]
    eventStoryEpisodes: Optional[List[EventStoryEpisode]]


class EventExchangeCost(Cost):
    id: Optional[int]
    eventExchangeId: Optional[int]


class EventExchange(ModelWithExtra):
    id: Optional[int]
    eventExchangeSummaryId: Optional[int]
    seq: Optional[int]
    resourceBoxId: Optional[int]
    exchangeLimit: Optional[int]
    eventExchangeCost: Optional[EventExchangeCost]


class EventExchangeSummary(ModelWithExtra):
    id: Optional[int]
    eventId: Optional[int]
    assetbundleName: Optional[str]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    eventExchanges: Optional[List[EventExchange]]


class EventStoryUnit(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    eventStoryId: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    eventStoryUnitRelation: Optional[Union[EventStoryUnitRelation, Unknown]]


class EventCard(ModelWithExtra):
    id: Optional[int]
    cardId: Optional[int]
    eventId: Optional[int]
    bonusRate: Optional[float]


class PreliminaryTournamentCard(ModelWithExtra):
    id: Optional[int]
    preliminaryTournamentId: Optional[int]
    cardId: Optional[int]


class PreliminaryTournamentMusic(ModelWithExtra):
    id: Optional[int]
    preliminaryTournamentId: Optional[int]
    musicDifficultyId: Optional[int]
    musicId: Optional[int]


class PreliminaryTournament(ModelWithExtra):
    id: Optional[int]
    preliminaryTournamentType: Optional[Union[PreliminaryTournamentType, Unknown]]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    releaseConditionId: Optional[int]
    preliminaryTournamentCards: Optional[List[PreliminaryTournamentCard]]
    preliminaryTournamentMusics: Optional[List[PreliminaryTournamentMusic]]


class CheerfulCarnivalSummary(ModelWithExtra):
    id: Optional[int]
    eventId: Optional[int]
    theme: Optional[str]
    midtermAnnounce1At: Optional[datetime]
    midtermAnnounce2At: Optional[datetime]
    assetbundleName: Optional[str]


class CheerfulCarnivalTeam(ModelWithExtra):
    id: Optional[int]
    eventId: Optional[int]
    seq: Optional[int]
    teamName: Optional[str]
    assetbundleName: Optional[str]


class CheerfulCarnivalPartyName(ModelWithExtra):
    id: Optional[int]
    partyName: Optional[str]
    gameCharacterUnitId1: Optional[int]
    gameCharacterUnitId2: Optional[int]
    gameCharacterUnitId3: Optional[int]
    gameCharacterUnitId4: Optional[int]
    gameCharacterUnitId5: Optional[int]


class CheerfulCarnivalCharacterPartyName(ModelWithExtra):
    id: Optional[int]
    characterPartyName: Optional[str]
    gameCharacterUnitId: Optional[int]


class CheerfulCarnivalLiveTeamPointBonus(ModelWithExtra):
    id: Optional[int]
    teamPointBonusRate: Optional[int]


class CheerfulCarnivalReward(ModelWithExtra):
    id: Optional[int]
    eventId: Optional[int]
    cheerfulCarnivalTeamId: Optional[int]
    resourceBoxId: Optional[int]


class CheerfulCarnivalResultReward(ModelWithExtra):
    id: Optional[int]
    eventId: Optional[int]
    cheerfulCarnivalTeamPointTermType: Optional[Union[CheerfulCarnivalTeamPointTermType, Unknown]]
    cheerfulCarnivalResultType: Optional[Union[CheerfulCarnivalResultType, Unknown]]
    resourceBoxId: Optional[int]


class Appeal(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    appealTargetType: Optional[Union[AppealTargetType, Unknown]]
    appealType: Optional[Union[AppealType, Unknown]]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    appealReadConditionType: Optional[Union[AppealReadConditionType, Unknown]]
    text: Optional[str]


class Boost(ModelWithExtra):
    id: Optional[int]
    costBoost: Optional[int]
    isEventOnly: Optional[bool]
    expRate: Optional[int]
    rewardRate: Optional[int]
    livePointRate: Optional[int]
    eventPointRate: Optional[int]
    bondsExpRate: Optional[int]


class BoostPresent(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    recoveryValue: Optional[int]
    presentLimit: Optional[int]
    assetbundleName: Optional[str]
    isUnlimitedReceive: Optional[bool]
    boostPresentCostId: Optional[int]


class BoostPresentCost(Cost):
    id: Optional[int]


class EpisodeCharacter(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    character2dId: Optional[int]
    storyType: Optional[Union[StoryType, Unknown]]
    episodeId: Optional[int]


class CustomProfileTextColor(ModelWithExtra):
    id: Optional[int]
    seq: Optional[int]
    colorCode: Optional[str]


class CustomProfileTextFont(ModelWithExtra):
    id: Optional[int]
    name: Optional[str]
    fontName: Optional[str]
    assetbundleName: Optional[str]


class CustomProfileResource(ModelWithExtra):
    customProfileResourceType: Optional[Union[CustomProfileResourceType, Unknown]]
    id: Optional[int]
    seq: Optional[int]
    name: Optional[str]
    resourceLoadType: Optional[Union[ResourceLoadType, Unknown]]
    resourceLoadVal: Optional[str]
    fileName: Optional[str]


class CustomProfilePlayerInfoResource(CustomProfileResource):
    pass


class CustomProfileGeneralBackgroundResource(CustomProfileResource):
    pass


class CustomProfileStoryBackgroundResource(CustomProfileResource):
    pass


class CustomProfileCollectionResource(CustomProfileResource):
    customProfileResourceCollectionType: Optional[Union[CustomProfileResourceCollectionType, Unknown]]
    groupId: Optional[int]


class CustomProfileMemberStandingPictureResource(CustomProfileResource):
    characterId: Optional[int]


class CustomProfileShapeResource(CustomProfileResource):
    pass


class CustomProfileEtcResource(CustomProfileResource):
    pass


class CustomProfileGachaBehavior(ModelWithExtra):
    id: Optional[int]
    customProfileGachaId: Optional[int]
    seq: Optional[int]
    costResourceType: Optional[Union[ResourceType, Unknown]]
    costResourceQuantity: Optional[int]
    spinCount: Optional[int]


class CustomProfileGachaDetail(ModelWithExtra):
    id: Optional[int]
    customProfileGachaId: Optional[int]
    customProfileResourceType: Optional[Union[CustomProfileResourceType, Unknown]]
    customProfileResourceId: Optional[int]
    customProfileResourceQuantity: Optional[int]
    weight: Optional[int]


class CustomProfileGacha(ModelWithExtra):
    id: Optional[int]
    name: Optional[str]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    assetbundleName: Optional[str]
    description: Optional[str]
    notice: Optional[str]
    customProfileGachaBehaviors: Optional[List[CustomProfileGachaBehavior]]
    customProfileGachaDetails: Optional[List[CustomProfileGachaDetail]]


class StreamingLiveBgm(ModelWithExtra):
    id: Optional[int]
    virtualLiveId: Optional[int]
    seq: Optional[int]
    musicVocalId: Optional[int]


class Omikuji(ModelWithExtra):
    id: Optional[int]
    omikujiGroupId: Optional[int]
    unit: Optional[Union[Unit, Unknown]]
    fortuneType: Optional[Union[FortuneType, Unknown]]
    summary: Optional[str]
    title1: Optional[str]
    description1: Optional[str]
    title2: Optional[str]
    description2: Optional[str]
    title3: Optional[str]
    description3: Optional[str]
    unitAssetbundleName: Optional[str]
    fortuneAssetbundleName: Optional[str]
    omikujiCoverAssetbundleName: Optional[str]
    unitFilePath: Optional[str]
    fortuneFilePath: Optional[str]
    omikujiCoverFilePath: Optional[str]


class OmikujiGroup(ModelWithExtra):
    id: Optional[int]
    name: Optional[str]
    summary: Optional[str]
    description: Optional[str]
    assetbundleName: Optional[str]
    appealAssetbundleName: Optional[str]
    soundAssetbundleName: Optional[str]


class OmikujiRate(ModelWithExtra):
    id: Optional[int]
    omikujiGroupId: Optional[int]
    fortuneType: Optional[Union[FortuneType, Unknown]]
    rate: Optional[float]


class OmikujiCost(Cost):
    id: Optional[int]
    omikujiGroupId: Optional[int]
    seq: Optional[int]


class OmikujiReward(ModelWithExtra):
    id: Optional[int]
    omikujiGroupId: Optional[int]
    seq: Optional[int]
    resourceType: Optional[Union[ResourceType, Unknown]]
    resourceId: Optional[int]
    resourceQuantity: Optional[int]


class VirtualBoothShop(ModelWithExtra):
    id: Optional[int]
    virtualLiveId: Optional[int]
    virtualBoothShopType: Optional[Union[VirtualBoothShopType, Unknown]]
    targetId: Optional[int]


class SpecialSeason(ModelWithExtra):
    id: Optional[int]
    specialSeasonType: Optional[Union[SpecialSeasonType, Unknown]]
    startAt: Optional[datetime]
    endAt: Optional[datetime]
    priority: Optional[int]


class SpecialSeasonArea(ModelWithExtra):
    id: Optional[int]
    specialSeasonId: Optional[int]
    areaId: Optional[int]
    assetbundleName: Optional[str]
    fileName: Optional[str]
    specialSeasonAreaUseType: Optional[Union[SpecialSeasonAreaUseType, Unknown]]


class RankMatchPenalty(ModelWithExtra):
    id: Optional[int]
    count: Optional[int]
    rankMatchPenaltyType: Optional[Union[RankMatchPenaltyType, Unknown]]
    rankMatchPenaltyTypeValue: Optional[int]


class RankMatchPlacement(ModelWithExtra):
    id: Optional[int]
    rankMatchPlacementConditionType: Optional[str]
    tierBehaviorType: Optional[Union[TierBehaviorType, Unknown]]
    tierBehaviorTypeValue: Optional[int]
    rankMatchPlacementConditionTypeValue: Optional[int]


class RankMatchBonusPointCondition(ModelWithExtra):
    id: Optional[int]
    rankMatchBonusPointConditionType: Optional[Union[RankMatchBonusPointConditionType, Unknown]]
    groupId: Optional[int]
    priority: Optional[int]
    calcType: Optional[Union[CalcType, Unknown]]
    bonusPoint: Optional[int]


class RankMatchSeasonPlayableTime(ModelWithExtra):
    id: Optional[int]
    rankMatchSeasonId: Optional[int]
    startTime: Optional[str]
    endTime: Optional[str]


class RankMatchSeasonTierMusicPlayLevel(ModelWithExtra):
    id: Optional[int]
    rankMatchSeasonId: Optional[int]
    rankMatchTierId: Optional[int]
    fromPlayLevel: Optional[int]
    toPlayLevel: Optional[int]


class RankMatchSeasonTierReward(ModelWithExtra):
    id: Optional[int]
    rankMatchSeasonId: Optional[int]
    rankMatchTierId: Optional[int]
    resourceBoxId: Optional[int]


class RankMatchSeason(ModelWithExtra):
    id: Optional[int]
    name: Optional[str]
    startAt: Optional[datetime]
    aggregatedAt: Optional[datetime]
    rankingPublishedAt: Optional[datetime]
    batchExecutionAt: Optional[datetime]
    distributionStartAt: Optional[datetime]
    distributionEndAt: Optional[datetime]
    closedAt: Optional[datetime]
    assetbundleName: Optional[str]
    isDisplayResult: Optional[bool]
    rankMatchSeasonPlayableTimes: Optional[List[RankMatchSeasonPlayableTime]]
    rankMatchSeasonTierMusicPlayLevels: Optional[
        List[RankMatchSeasonTierMusicPlayLevel]
    ]
    rankMatchSeasonTierRewards: Optional[List[RankMatchSeasonTierReward]]


class RankMatchTier(ModelWithExtra):
    id: Optional[int]
    rankMatchGradeId: Optional[int]
    rankMatchClassId: Optional[int]
    tier: Optional[int]
    totalMusicDifficulty: Optional[int]
    point: Optional[int]
    gradeAssetbundleName: Optional[str]
    tierAssetbundleName: Optional[str]


class RankMatchTierBonusPoint(ModelWithExtra):
    id: Optional[int]
    rankMatchTierId: Optional[int]
    maxBonusPoint: Optional[int]
    rewardPoint: Optional[int]


class RankMatchGrade(Costume2dGroup):
    id: Optional[int]
    name: Optional[str]


class RankMatchClass(Costume2dGroup):
    id: Optional[int]
    name: Optional[str]


class LimitedTitleScreen(ModelWithExtra):
    id: Optional[int]
    priority: Optional[int]
    downloadStartAt: Optional[datetime]
    downloadEndAt: Optional[datetime]
    displayStartAt: Optional[datetime]
    displayEndAt: Optional[datetime]
    bgAssetbundleName: Optional[str]
    logoAssetbundleName: Optional[str]
    bgmAssetbundleName: Optional[str]
    startEffectAssetbundleName: Optional[str]


class MasterData(ModelWithExtra):
    gameCharacters: Optional[List[GameCharacter]]
    gameCharacterUnits: Optional[List[GameCharacterUnit]]
    outsideCharacters: Optional[List[OutsideCharacter]]
    character3ds: Optional[List[Character3d]]
    character2ds: Optional[List[Character2d]]
    characterProfiles: Optional[List[CharacterProfile]]
    bonds: Optional[List[Bond]]
    bondsLive2ds: Optional[List[BondsLive2d]]
    bondsRankUpLive2ds: Optional[List[BondsRankUpLive2d]]
    unitProfiles: Optional[List[UnitProfile]]
    actionSets: Optional[List[ActionSet]]
    areas: Optional[List[Area]]
    areaPlaylists: Optional[List[AreaPlaylist]]
    mobCharacters: Optional[List[MobCharacter]]
    characterCostumes: Optional[List[CharacterCostume]]
    cardCostume3ds: Optional[List[CardCostume3d]]
    cards: Optional[List[Card]]
    skills: Optional[List[Skill]]
    cardEpisodes: Optional[List[CardEpisode]]
    cardRarities: Optional[List[CardRarity]]
    cardSkillCosts: Optional[List[CardSkillCost]]
    musics: Optional[List[Music]]
    musicTags: Optional[List[MusicTag]]
    musicDifficulties: Optional[List[MusicDifficulty]]
    musicVocals: Optional[List[MusicVocal]]
    musicDanceMembers: Optional[List[MusicDanceMember]]
    musicAchievements: Optional[List[MusicAchievement]]
    musicVideoCharacters: Optional[List[MusicVideoCharacter]]
    musicAssetVariants: Optional[List[MusicAssetVariant]]
    musicCollaborations: Optional[List[MusicCollaboration]]
    episodeMusicVideoCostumes: Optional[List[EpisodeMusicVideoCostume]]
    releaseConditions: Optional[List[ReleaseCondition]]
    playLevelScores: Optional[List[PlayLevelScore]]
    ingameCombos: Optional[List[IngameCombo]]
    ingameNotes: Optional[List[IngameNote]]
    ingameNoteJudges: Optional[List[IngameNoteJudge]]
    ingamePlayLevels: Optional[List[IngamePlayLevel]]
    ingameCutins: Optional[List[IngameCutin]]
    ingameCutinCharacters: Optional[List[IngameCutinCharacter]]
    ingameJudgeFrames: Optional[List[IngameJudgeFrame]]
    ingameNoteJudgeTechnicalScores: Optional[List[IngameNoteJudgeTechnicalScore]]
    shops: Optional[List[Shop]]
    shopItems: Optional[List[ShopItem]]
    costume3dShopItems: Optional[List[Costume3dShopItem]]
    areaItems: Optional[List[AreaItem]]
    areaItemLevels: Optional[List[AreaItemLevel]]
    materials: Optional[List[Material]]
    gachas: Optional[List[Gacha]]
    gachaBonuses: Optional[List[GachaBonus]]
    gachaBonusPoints: Optional[List[GachaBonusPoint]]
    gachaExtras: Optional[List[GachaExtra]]
    giftGachaExchanges: Optional[List[GiftGachaExchange]]
    gachaTabs: Optional[List[Union[dict, str, int]]]
    practiceTickets: Optional[List[PracticeTicket]]
    skillPracticeTickets: Optional[List[SkillPracticeTicket]]
    levels: Optional[List[Level]]
    unitStories: Optional[List[UnitStory]]
    specialStories: Optional[List[SpecialStory]]
    configs: Optional[List[Config]]
    clientConfigs: Optional[List[ClientConfig]]
    wordings: Optional[List[Wording]]
    costume3ds: Optional[List[Costume3d]]
    costume3dModels: Optional[List[Costume3dModel]]
    costume3dModelAvailablePatterns: Optional[List[Costume3dModelAvailablePattern]]
    gameCharacterUnit3dMotions: Optional[List[GameCharacterUnit3dMotion]]
    costume2ds: Optional[List[Costume2d]]
    costume2dGroups: Optional[List[Costume2dGroup]]
    topics: Optional[List[Topic]]
    liveStages: Optional[List[LiveStage]]
    stamps: Optional[List[Stamp]]
    multiLiveLobbies: Optional[List[MultiLiveLobby]]
    masterLessons: Optional[List[MasterLesson]]
    masterLessonRewards: Optional[List[MasterLessonReward]]
    cardExchangeResources: Optional[List[CardExchangeResource]]
    materialExchanges: Optional[List[MaterialExchange]]
    materialExchangeSummaries: Optional[List[MaterialExchangeSummary]]
    boostItems: Optional[List[BoostItem]]
    billingProducts: Optional[List[BillingProduct]]
    billingShopItems: Optional[List[BillingShopItem]]
    billingShopItemExchangeCosts: Optional[List[BillingShopItemExchangeCost]]
    colorfulPasses: Optional[List[ColorfulPass]]
    jewelBehaviors: Optional[List[JewelBehavior]]
    characterRanks: Optional[List[CharacterRank]]
    characterMissionV2s: Optional[List[CharacterMissionV2]]
    characterMissionV2ParameterGroups: Optional[List[CharacterMissionV2ParameterGroup]]
    characterMissionV2AreaItems: Optional[List[CharacterMissionV2AreaItem]]
    systemLive2ds: Optional[List[SystemLive2d]]
    normalMissions: Optional[List[NormalMission]]
    beginnerMissions: Optional[List[BeginnerMission]]
    resourceBoxes: Optional[List[ResourceBox]]
    liveMissionPeriods: Optional[List[LiveMissionPeriod]]
    liveMissions: Optional[List[LiveMission]]
    liveMissionPasses: Optional[List[LiveMissionPass]]
    penlightColors: Optional[List[PenlightColor]]
    penlights: Optional[List[Penlight]]
    liveTalks: Optional[List[LiveTalk]]
    tips: Optional[List[Tip]]
    gachaCeilItems: Optional[List[GachaCeilItem]]
    gachaCeilExchangeSummaries: Optional[List[GachaCeilExchangeSummary]]
    playerRankRewards: Optional[List[PlayerRankReward]]
    gachaTickets: Optional[List[GachaTicket]]
    honorGroups: Optional[List[HonorGroup]]
    honors: Optional[List[Honor]]
    honorMissions: Optional[List[HonorMission]]
    bondsHonors: Optional[List[BondsHonor]]
    bondsHonorWords: Optional[List[BondsHonorWord]]
    bondsRewards: Optional[List[BondsReward]]
    challengeLives: Optional[List[ChallengeLive]]
    challengeLiveDecks: Optional[List[ChallengeLiveDeck]]
    challengeLiveStages: Optional[List[ChallengeLiveStage]]
    challengeLiveStageExs: Optional[List[ChallengeLiveStageEx]]
    challengeLiveHighScoreRewards: Optional[List[ChallengeLiveHighScoreReward]]
    challengeLiveCharacters: Optional[List[ChallengeLiveCharacter]]
    challengeLivePlayDayRewardPeriods: Optional[List[ChallengeLivePlayDayRewardPeriod]]
    virtualLives: Optional[List[VirtualLive]]
    virtualShops: Optional[List[VirtualShop]]
    virtualItems: Optional[List[VirtualItem]]
    virtualLiveCheerMessages: Optional[List[VirtualLiveCheerMessage]]
    virtualLiveCheerMessageDisplayLimits: Optional[
        List[VirtualLiveCheerMessageDisplayLimit]
    ]
    virtualLiveTickets: Optional[List[VirtualLiveTicket]]
    virtualLivePamphlets: Optional[List[VirtualLivePamphlet]]
    avatarAccessories: Optional[List[AvatarAccessory]]
    avatarCostumes: Optional[List[AvatarCostume]]
    avatarMotions: Optional[List[AvatarMotion]]
    avatarSkinColors: Optional[List[AvatarSkinColor]]
    avatarCoordinates: Optional[List[AvatarCoordinate]]
    ngWords: Optional[List[NgWord]]
    ruleSlides: Optional[List[RuleSlide]]
    facilities: Optional[List[Facility]]
    oneTimeBehaviors: Optional[List[OneTimeBehavior]]
    loginBonuses: Optional[List[LoginBonus]]
    beginnerLoginBonuses: Optional[List[BeginnerLoginBonus]]
    beginnerLoginBonusSummaries: Optional[List[BeginnerLoginBonusSummary]]
    limitedLoginBonuses: Optional[List[LimitedLoginBonus]]
    loginBonusLive2ds: Optional[List[LoginBonusLive2d]]
    events: Optional[List[Event]]
    eventMusics: Optional[List[EventMusic]]
    eventDeckBonuses: Optional[List[EventDeckBonus]]
    eventRarityBonusRates: Optional[List[EventRarityBonusRate]]
    eventItems: Optional[List[EventItem]]
    eventStories: Optional[List[EventStory]]
    eventExchangeSummaries: Optional[List[EventExchangeSummary]]
    eventStoryUnits: Optional[List[EventStoryUnit]]
    eventCards: Optional[List[EventCard]]
    preliminaryTournaments: Optional[List[PreliminaryTournament]]
    cheerfulCarnivalSummaries: Optional[List[CheerfulCarnivalSummary]]
    cheerfulCarnivalTeams: Optional[List[CheerfulCarnivalTeam]]
    cheerfulCarnivalPartyNames: Optional[List[CheerfulCarnivalPartyName]]
    cheerfulCarnivalCharacterPartyNames: Optional[
        List[CheerfulCarnivalCharacterPartyName]
    ]
    cheerfulCarnivalLiveTeamPointBonuses: Optional[
        List[CheerfulCarnivalLiveTeamPointBonus]
    ]
    cheerfulCarnivalRewards: Optional[List[CheerfulCarnivalReward]]
    cheerfulCarnivalResultRewards: Optional[List[CheerfulCarnivalResultReward]]
    appeals: Optional[List[Appeal]]
    boosts: Optional[List[Boost]]
    boostPresents: Optional[List[BoostPresent]]
    boostPresentCosts: Optional[List[BoostPresentCost]]
    episodeCharacters: Optional[List[EpisodeCharacter]]
    customProfileTextColors: Optional[List[CustomProfileTextColor]]
    customProfileTextFonts: Optional[List[CustomProfileTextFont]]
    customProfilePlayerInfoResources: Optional[List[CustomProfilePlayerInfoResource]]
    customProfileGeneralBackgroundResources: Optional[
        List[CustomProfileGeneralBackgroundResource]
    ]
    customProfileStoryBackgroundResources: Optional[
        List[CustomProfileStoryBackgroundResource]
    ]
    customProfileCollectionResources: Optional[List[CustomProfileCollectionResource]]
    customProfileMemberStandingPictureResources: Optional[
        List[CustomProfileMemberStandingPictureResource]
    ]
    customProfileShapeResources: Optional[List[CustomProfileShapeResource]]
    customProfileEtcResources: Optional[List[CustomProfileEtcResource]]
    customProfileMemberResourceExcludeCards: Optional[List[Union[dict, str, int]]]
    customProfileGachas: Optional[List[CustomProfileGacha]]
    customProfileGachaTabs: Optional[List[Union[dict, str, int]]]
    streamingLiveBgms: Optional[List[StreamingLiveBgm]]
    omikujis: Optional[List[Omikuji]]
    omikujiGroups: Optional[List[OmikujiGroup]]
    omikujiRates: Optional[List[OmikujiRate]]
    omikujiCosts: Optional[List[OmikujiCost]]
    omikujiRewards: Optional[List[OmikujiReward]]
    virtualBoothShops: Optional[List[VirtualBoothShop]]
    specialSeasons: Optional[List[SpecialSeason]]
    specialSeasonAreas: Optional[List[SpecialSeasonArea]]
    rankMatchPenalties: Optional[List[RankMatchPenalty]]
    rankMatchPlacements: Optional[List[RankMatchPlacement]]
    rankMatchBonusPointConditions: Optional[List[RankMatchBonusPointCondition]]
    rankMatchSeasons: Optional[List[RankMatchSeason]]
    rankMatchTiers: Optional[List[RankMatchTier]]
    rankMatchTierBonusPoints: Optional[List[RankMatchTierBonusPoint]]
    rankMatchGrades: Optional[List[RankMatchGrade]]
    rankMatchClasses: Optional[List[RankMatchClass]]
    limitedTitleScreens: Optional[List[LimitedTitleScreen]]
    panelMissionCampaigns: Optional[List[Union[dict, str, int]]]
