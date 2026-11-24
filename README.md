# The Funniest Out-of-Office

[![make.fun · u-kreutzx-the-funniest-out-of-office-054815cf](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)
[![rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/kunala23/u-kreutzx-the-funniest-out-of-office-054815cf/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf/leaderboard)
[![reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/kunala23/u-kreutzx-the-funniest-out-of-office-054815cf/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf)

Entry for the [make.fun](https://make.fun) competition
**The Funniest Out-of-Office** (`u-kreutzx-the-funniest-out-of-office-054815cf`).

## What it does

`main.py` writes a single line of out-of-office auto-reply — the funniest
one line we could write — to `/output/entry.txt`, in 140 characters or fewer:

> I'm out of office until Monday. My cat is covering my inbox. She has deleted three emails so far and feels absolutely nothing.

The line was written against the judge's brief: a one-line reply a real
person would actually set, turning on a genuine surprise (the inbox handed
to someone spectacularly unqualified), in a personal voice, with no wasted
words.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

No dependencies, no network, no configuration. The program validates its
own output: a single non-empty line of at most 140 characters, written as
UTF-8.

## License

MIT — see [LICENSE](LICENSE).
