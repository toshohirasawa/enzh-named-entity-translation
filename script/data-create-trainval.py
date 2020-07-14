from tqdm import tqdm

wiki_en = [l.strip() for l in open('./../wikititles-v2/zh-en/clean.en')]
wiki_zh = [l.strip() for l in open('./../wikititles-v2/zh-en/clean.zh')]

nyse_en = [l.strip().lower() for l in open('./../wikititles-company/test.en')]
nyse_zh = [l.strip().lower() for l in open('./../wikititles-company/test.zh')]
nyse = [(e, z) for e, z in zip(nyse_en, nyse_zh)]

def matches_com(title_en, title_zh, coms):
    '''Excludes titles matching coms'''
    if (title_en, title_zh) in coms:
        return True
    return False

def contains_com(title_en, title_zh, coms):
    '''Excludes titles containing coms in both English/Chinese side'''
    matches = map(lambda t: (t[0] in title_en) and (t[1] in title_zh), coms)
    if any(matches):
        return True
    return False

trainval_wiki = [[e, z] for e, z in tqdm(zip(wiki_en, wiki_zh)) if not contains_com(e.lower(), z.lower(), nyse)]

trainval_en = [i[0] for i in trainval_wiki]
trainval_zh = [i[1] for i in trainval_wiki]

print('\n'.join(trainval_en), file=open('./train.en', 'w'))
print('\n'.join(trainval_zh), file=open('./train.zh', 'w'))
