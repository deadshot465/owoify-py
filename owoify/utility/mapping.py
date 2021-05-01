from owoify.structures.word import Word
import random
import re

O_TO_OWO = re.compile(r'o')
EW_TO_UWU = re.compile(r'ew')
HEY_TO_HAY = re.compile(r'([Hh])ey')
DEAD_TO_DED_UPPER = re.compile(r'Dead')
DEAD_TO_DED_LOWER = re.compile(r'dead')
N_VOWEL_T_TO_ND = re.compile(r'n[aeiou]*t')
READ_TO_WEAD_UPPER = re.compile(r'Read')
READ_TO_WEAD_LOWER = re.compile(r'read')
BRACKETS_TO_STARTRAILS_FORE = re.compile(r'[({<]')
BRACKETS_TO_STARTRAILS_REAR = re.compile(r'[)}>]')
PERIOD_COMMA_EXCLAMATION_SEMICOLON_TO_KAOMOJIS_FIRST = re.compile(r'[.,](?![0-9])')
PERIOD_COMMA_EXCLAMATION_SEMICOLON_TO_KAOMOJIS_SECOND = re.compile(r'[!;]+')
THAT_TO_DAT_UPPER = re.compile(r'That')
THAT_TO_DAT_LOWER = re.compile(r'that')
TH_TO_F_UPPER = re.compile(r'TH(?!E)')
TH_TO_F_LOWER = re.compile(r'[Tt]h(?![Ee])')
LE_TO_WAL = re.compile(r'le$')
VE_TO_WE_UPPER = re.compile(r'Ve')
VE_TO_WE_LOWER = re.compile(r've')
RY_TO_WWY = re.compile(r'ry')
RORL_TO_W_UPPER = re.compile(r'(?:R|L)')
RORL_TO_W_LOWER = re.compile(r'(?:r|l)')
LL_TO_WW = re.compile(r'll')
VOWEL_OR_R_EXCEPT_O_L_TO_WL_UPPER = re.compile(r'[AEIUR]([lL])$')
VOWEL_OR_R_EXCEPT_O_L_TO_WL_LOWER = re.compile(r'[aeiur]l$')
OLD_TO_OWLD_UPPER = re.compile(r'OLD')
OLD_TO_OWLD_LOWER = re.compile(r'([Oo])ld')
OL_TO_OWL_UPPER = re.compile(r'OL')
OL_TO_OWL_LOWER = re.compile(r'([Oo])l')
LORR_O_TO_WO_UPPER = re.compile(r'[LR]([oO])')
LORR_O_TO_WO_LOWER = re.compile(r'[lr]o')
SPECIFIC_CONSONANTS_O_TO_LETTER_AND_WO_UPPER = re.compile(r'([BCDFGHJKMNPQSTXYZ])([oO])')
SPECIFIC_CONSONANTS_O_TO_LETTER_AND_WO_LOWER = re.compile(r'([bcdfghjkmnpqstxyz])o')
VORW_LE_TO_WAL = re.compile(r'[vw]le')
FI_TO_FWI_UPPER = re.compile(r'FI')
FI_TO_FWI_LOWER = re.compile(r'([Ff])i')
VER_TO_WER = re.compile(r'([Vv])er')
POI_TO_PWOI = re.compile(r'([Pp])oi')
SPECIFIC_CONSONANTS_LE_TO_LETTER_AND_WAL = re.compile(r'([DdFfGgHhJjPpQqRrSsTtXxYyZz])le$')
CONSONANT_R_TO_CONSONANT_W = re.compile(r'([BbCcDdFfGgKkPpQqSsTtWwXxZz])r')
LY_TO_WY_UPPER = re.compile(r'Ly')
LY_TO_WY_LOWER = re.compile(r'ly')
PLE_TO_PWE = re.compile(r'([Pp])le')
NR_TO_NW_UPPER = re.compile(r'NR')
NR_TO_NW_LOWER = re.compile(r'nr')
FUC_TO_FWUC = re.compile(r'([Ff])uc')
MOM_TO_MWOM = re.compile(r'([Mm])om')
ME_TO_MWE = re.compile(r'([Mm])e')
N_VOWEL_TO_NY_FIRST = re.compile(r'n([aeiou])')
N_VOWEL_TO_NY_SECOND = re.compile(r'N([aeiou])')
N_VOWEL_TO_NY_THIRD = re.compile(r'N([AEIOU])')
OVE_TO_UV_UPPER = re.compile(r'OVE')
OVE_TO_UV_LOWER = re.compile(r'ove')
HAHA_TO_HEHE_XD = re.compile(r'\b(ha|hah|heh|hehe)+\b')
THE_TO_TEH = re.compile(r'\b([Tt])he\b')
YOU_TO_U_UPPER = re.compile(r'\bYou\b')
YOU_TO_U_LOWER = re.compile(r'\byou\b')
TIME_TO_TIM = re.compile(r'\b([Tt])ime\b')
OVER_TO_OWOR = re.compile(r'([Oo])ver')
WORSE_TO_WOSE = re.compile(r'([Ww])orse')

# Additional kaomojis come from [owoify](https://pypi.org/project/owoify/) and Discord.
FACES = [
    '(・`ω´・)', ';;w;;', 'owo', 'UwU', '>w<', '^w^', '(* ^ ω ^)',
    '(⌒ω⌒)', 'ヽ(*・ω・)ﾉ', '(o´∀`o)', '(o･ω･o)', '＼(＾▽＾)／',
    '(*^ω^)', '(◕‿◕✿)', '(◕ᴥ◕)', 'ʕ•ᴥ•ʔ', 'ʕ￫ᴥ￩ʔ', '(*^.^*)', '(｡♥‿♥｡)',
    'OwO', 'uwu', 'uvu', 'UvU', '(*￣з￣)', '(つ✧ω✧)つ', '(/ =ω=)/',
    '(╯°□°）╯︵ ┻━┻', '┬─┬ ノ( ゜-゜ノ)', '¯\\_(ツ)_/¯'
]


def map_o_to_owo(input: Word) -> Word:
    replacement: str
    if random.randint(0, 2) > 0:
        replacement = 'owo'
    else:
        replacement = 'o'
    return input.replace(O_TO_OWO, replacement)


def map_ew_to_uwu(input: Word) -> Word:
    return input.replace(EW_TO_UWU, 'uwu')


def map_hey_to_hay(input: Word) -> Word:
    return input.replace(HEY_TO_HAY, '\\1ay')


def map_dead_to_ded(input: Word) -> Word:
    return input.replace(DEAD_TO_DED_UPPER, 'Ded') \
        .replace(DEAD_TO_DED_LOWER, 'ded')


def map_n_vowel_t_to_nd(input: Word) -> Word:
    return input.replace(N_VOWEL_T_TO_ND, 'nd')


def map_read_to_wead(input: Word) -> Word:
    return input.replace(READ_TO_WEAD_UPPER, 'Wead') \
        .replace(READ_TO_WEAD_LOWER, 'wead')


def map_brackets_to_star_trails(input: Word) -> Word:
    return input.replace(BRACKETS_TO_STARTRAILS_FORE, '｡･:*:･ﾟ★,｡･:*:･ﾟ☆') \
        .replace(BRACKETS_TO_STARTRAILS_REAR, '☆ﾟ･:*:･｡,★ﾟ･:*:･｡')


def map_period_comma_exclamation_semicolon_to_kaomojis(input: Word) -> Word:
    return input.replace_with_func_single(PERIOD_COMMA_EXCLAMATION_SEMICOLON_TO_KAOMOJIS_FIRST,
                                          lambda: f' {FACES[random.randint(0, len(FACES) - 1)]}') \
        .replace_with_func_single(PERIOD_COMMA_EXCLAMATION_SEMICOLON_TO_KAOMOJIS_SECOND,
                                  lambda: f' {FACES[random.randint(0, len(FACES) - 1)]}')


def map_that_to_dat(input: Word) -> Word:
    return input.replace(THAT_TO_DAT_LOWER, 'dat') \
        .replace(THAT_TO_DAT_UPPER, 'Dat')


def map_th_to_f(input: Word) -> Word:
    return input.replace(TH_TO_F_LOWER, 'f') \
        .replace(TH_TO_F_UPPER, 'F')


def map_le_to_wal(input: Word) -> Word:
    return input.replace(LE_TO_WAL, 'wal')


def map_ve_to_we(input: Word) -> Word:
    return input.replace(VE_TO_WE_LOWER, 'we') \
        .replace(VE_TO_WE_UPPER, 'We')


def map_ry_to_wwy(input: Word) -> Word:
    return input.replace(RY_TO_WWY, 'wwy')


def map_r_or_l_to_w(input: Word) -> Word:
    return input.replace(RORL_TO_W_LOWER, 'w') \
        .replace(RORL_TO_W_UPPER, 'W')


def map_ll_to_ww(input: Word) -> Word:
    return input.replace(LL_TO_WW, 'ww')


def map_vowel_or_r_except_o_l_to_wl(input: Word) -> Word:
    return input.replace(VOWEL_OR_R_EXCEPT_O_L_TO_WL_LOWER, 'wl') \
        .replace(VOWEL_OR_R_EXCEPT_O_L_TO_WL_UPPER, 'W\\1')


def map_old_to_owld(input: Word) -> Word:
    return input.replace(OLD_TO_OWLD_LOWER, '\\1wld') \
        .replace(OLD_TO_OWLD_UPPER, 'OWLD')


def map_ol_to_owl(input: Word) -> Word:
    return input.replace(OL_TO_OWL_LOWER, '\\1wl') \
        .replace(OL_TO_OWL_UPPER, 'OWL')


def map_l_or_r_o_to_wo(input: Word) -> Word:
    return input.replace(LORR_O_TO_WO_LOWER, 'wo') \
        .replace(LORR_O_TO_WO_UPPER, 'W\\1')


def mapping_function_1(s1: str, s2: str) -> str:
    msg = s1
    if s2.upper() == s2:
        msg += 'W'
    else:
        msg += 'w'
    msg += s2
    return msg


def map_specific_consonants_o_to_letter_and_wo(input: Word) -> Word:
    return input.replace(SPECIFIC_CONSONANTS_O_TO_LETTER_AND_WO_LOWER, '\\1wo') \
        .replace_with_func_multiple(SPECIFIC_CONSONANTS_O_TO_LETTER_AND_WO_UPPER, mapping_function_1)


def map_v_or_w_le_to_wal(input: Word) -> Word:
    return input.replace(VORW_LE_TO_WAL, 'wal')


def map_fi_to_fwi(input: Word) -> Word:
    return input.replace(FI_TO_FWI_LOWER, '\\1wi') \
        .replace(FI_TO_FWI_UPPER, 'FWI')


def map_ver_to_wer(input: Word) -> Word:
    return input.replace(VER_TO_WER, 'wer')


def map_poi_to_pwoi(input: Word) -> Word:
    return input.replace(POI_TO_PWOI, '\\1woi')


def map_specific_consonants_le_to_letter_and_wal(input: Word) -> Word:
    return input.replace(SPECIFIC_CONSONANTS_LE_TO_LETTER_AND_WAL, '\\1wal')


def map_consonant_r_to_consonant_w(input: Word) -> Word:
    return input.replace(CONSONANT_R_TO_CONSONANT_W, '\\1w')


def map_ly_to_wy(input: Word) -> Word:
    return input.replace(LY_TO_WY_LOWER, 'wy') \
        .replace(LY_TO_WY_UPPER, 'Wy')


def map_ple_to_pwe(input: Word) -> Word:
    return input.replace(PLE_TO_PWE, '\\1we')


def map_nr_to_nw(input: Word) -> Word:
    return input.replace(NR_TO_NW_LOWER, 'nw') \
        .replace(NR_TO_NW_UPPER, 'NW')


def map_fuc_to_fwuc(input: Word) -> Word:
    return input.replace(FUC_TO_FWUC, '\\1wuc')


def map_mom_to_mwom(input: Word) -> Word:
    return input.replace(MOM_TO_MWOM, '\\1wom')


def map_me_to_mwe(input: Word) -> Word:
    return input.replace(ME_TO_MWE, '\\1we')


def map_n_vowel_to_ny(input: Word) -> Word:
    return input.replace(N_VOWEL_TO_NY_FIRST, 'ny\\1') \
        .replace(N_VOWEL_TO_NY_SECOND, 'Ny\\1') \
        .replace(N_VOWEL_TO_NY_THIRD, 'NY\\1')


def map_ove_to_uv(input: Word) -> Word:
    return input.replace(OVE_TO_UV_LOWER, 'uv') \
        .replace(OVE_TO_UV_UPPER, 'UV')


def map_haha_to_hehe_xd(input: Word) -> Word:
    return input.replace(HAHA_TO_HEHE_XD, 'hehe xD')


def map_the_to_teh(input: Word) -> Word:
    return input.replace(THE_TO_TEH, '\\1eh')


def map_you_to_u(input: Word) -> Word:
    return input.replace(YOU_TO_U_UPPER, 'U') \
        .replace(YOU_TO_U_LOWER, 'u')


def map_time_to_tim(input: Word) -> Word:
    return input.replace(TIME_TO_TIM, '\\1im')


def map_over_to_owor(input: Word) -> Word:
    return input.replace(OVER_TO_OWOR, '\\1wor')


def map_worse_to_wose(input: Word) -> Word:
    return input.replace(WORSE_TO_WOSE, '\\1ose')
