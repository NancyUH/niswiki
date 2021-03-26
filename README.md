# NISLAB Wiki

ネットワーク情報システム研究室（NISLAB Wiki）  
Network Information Systems Lab Wiki

> NISLAB Wiki は [こちら](https://wiki.nislab.io/)  
> <https://wiki.nislab.io/>

## 目次

1. [NISLAB Wiki の編集手順](#nislab-wiki-%E3%81%AE%E7%B7%A8%E9%9B%86%E6%89%8B%E9%A0%86)
   1. [環境構築](#%E7%92%B0%E5%A2%83%E6%A7%8B%E7%AF%89)
   2. [プロジェクトのフォーク・クローン](#%E3%83%AA%E3%83%9D%E3%82%B8%E3%83%88%E3%83%AA%E3%81%AE%E3%83%95%E3%82%A9%E3%83%BC%E3%82%AF%E3%82%AF%E3%83%AD%E3%83%BC%E3%83%B3)
   3. [ページの追加・編集](#%E3%83%9A%E3%83%BC%E3%82%B8%E3%81%AE%E8%BF%BD%E5%8A%A0%E7%B7%A8%E9%9B%86)
   4. [編集完了後の公開手順](#%E7%B7%A8%E9%9B%86%E5%AE%8C%E4%BA%86%E5%BE%8C%E3%81%AE%E5%85%AC%E9%96%8B%E6%89%8B%E9%A0%86)
2. [仕組み](#%E4%BB%95%E7%B5%84%E3%81%BF)

## NISLAB Wiki の編集手順

基本的に Mac で編集することを前提として記載しています。  
Windows を使用している人は、適宜調べながら作業を行ってください。

### 環境構築

これらがインストールされている必要があります。

- Homebrew
- git
- Node
- Hugo

Terminal から下記のコマンドを叩いて、必要なパッケージがインストールされているか確認してください。  
バージョンが表示されればインストールされているので問題ありません。

> 下記の 3 つがインストールされていない人は、MacOS 用のパッケージ管理システムである Homebrew を用いてインストールを行ってください。
>
> - git がインストールされていない場合は `brew install git`
> - Node がインストールされていない場合は [Qiita の記事](https://qiita.com/kyosuke5_20/items/c5f68fc9d89b84c0df09) を参考に。
> - Hugo がインストールされていない場合は `brew install hugo`

```sh
# Homebrew の確認
brew -v

# git の確認
git --version

# Node Package Manager の確認
npm -v

# Hugo の確認
hugo version
```

特段の理由がない場合、これらをアップデートすることを推奨していますので、下記のコマンドからパッケージのアップデートを行ってください。

> 下記のコマンドの実行には数分かかることがありますので、安定した回線で実行してください

```sh
# Homebrew のアップデート
brew update

# Homebrew + パッケージ のアップデート
brew upgrade
```

[GitHub](https://github.com/) への登録が必要ですので、アカウントの作成を行ってください。

> GitHub で ssh 接続できるようにしておくと何かと便利ですので、 [Qiita の記事](https://qiita.com/shizuma/items/2b2f873a0034839e47ce) などを参考にしておくと良いかも。

### リポジトリのフォーク・クローン

> こちらの [Qiita の記事](https://qiita.com/YumaInaura/items/acff806290c8953d3185) を参考にしていただくことで簡単にフォークすることができます。

GitHub で管理されているプロジェクトをローカルに落として、適宜編集を行います。  
必要なパッケージのインストールも行います。

```sh
# デスクトップへディレクトリを移動
cd
cd Desktop/

# プロジェクトをクローン
git clone GITHUB_YOUR_FORKED_REPOSITORY_URL

# プロジェクトのディレクトリに移動
cd niswiki

# パッケージのインストール
npm install
```

### ページの追加・編集

できれば、GitHub Issue を用いて管理すべきですが、必須ではありませんので、興味のある人のみ適宜調べて作業してください。  
基本的には、各自でブランチを切ってもらい、作業をおこない、GitHub 上でマージしてもらう形になるかと思います。

```sh
# フォーク元のリモートリポジトリを upstream として設定
git remote add upstream https://github.com/Kenny-NISLab/niswiki.git

# 最新のリモートリポジトリを取得
git pull upstream develop
```

ページを編集するには、プロジェクトの `content/` 以下を編集します。  
記事を追加する場合は、以下のコマンドから追加できます。

```sh
# content/guidance/ 配下に xx という記事を追加する場合
hugo new guidance/xx/_index.md
```

記事は `Markdown` で記述します。 記法については、 [Qiita の記事](https://qiita.com/tbpgr/items/989c6badefff69377da7) などを参考にしてください。  
編集した NISLAB Wiki については、下記コマンドを実行することで、ローカルホストで実行することができます。

```zsh
# ローカルホストで実行
npm start

# 下記アドレスを Chrome 等に貼り付けて表示確認できます
http://localhost:1313

# 実行を止めたい場合は
Control + C
```

### 編集完了後の公開手順

編集が完了したら、記事を公開するために下記コマンドを実行してください。

```zsh
# フォーマットを実行
npm run format

# 全てのファイルをインデックスに追加
git add .

# インデックスに追加したファイルをコミット
git commit -m "何を変更したのかコメントとしてここに記述"

# リモートリポジトリにアップロード
git push origin "作業開始時に指定したブランチ名"
```

GitHub 上で元のリポジトリに Pull Request する必要があります。  
先ほどアップロードしたブランチが GitHub 上に反映されていると思いますので、フォーク元のリポジトリへプルリクエストを作成して、マージを行ってください。  
マージが完了すると CI/CD が走り、自動的に <https://wiki.nislab.io/> に反映されます。

## 仕組み

[NISLAB Wiki](https://wiki.nislab.io/) は [Hugo](https://gohugo.io) を用いて開発されています。  
Hugo は Go をベースとした SSG であり、基本的に HTML/CSS の知識さえあれば自由に Web サイトを構築することが可能です。  
Go をベースとしているので、様々な OS 上で動作するだけでなく、Docker 上でも使用できます。

CI/CD に関しては、aws Amplify を GitHub と連携させることで、main ブランチにマージされる度にビルド・デプロイが実行されます。  
aws Amplify はコンテンツが更新される度に CDN キャッシュが無効化されるため、ページを高速に表示することができるだけでなく、更新されたコンテンツが即時に反映されます。

ページのアクセス元解析の観点から、[Google Analytics](https://analytics.google.com/) も組み込まれています。

## Contributors

- RSugimoto
- KHosono
