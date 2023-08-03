CREATE MIGRATION m1bzwu6sgqtampqxktp6255rl6m27qxz5cbhc4bmuuqm5aombmorga
    ONTO m1k5kycleusgqjihfxcureupydou6fjrde3awjkelkrzlkdvi6fika
{
  ALTER TYPE default::News {
      ALTER LINK author {
          SET REQUIRED USING (<default::User>{});
      };
  };
};
