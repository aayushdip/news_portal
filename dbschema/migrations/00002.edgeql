CREATE MIGRATION m1gvavphaa53m3lax7wetipag2q3tems4wryod7bvvvlsfc7br7xoq
    ONTO m12xjv24iyhrmd3eqnir2e3kxgsi62o6z6kuiofboag356zuqayi4a
{
  ALTER TYPE default::News {
      CREATE PROPERTY admin: std::bool {
          SET REQUIRED USING (<std::bool>{});
      };
      CREATE PROPERTY email: std::str {
          SET REQUIRED USING (<std::str>{});
      };
      CREATE PROPERTY hashed_password: std::str {
          SET REQUIRED USING (<std::str>{});
      };
      CREATE PROPERTY name: std::str {
          SET REQUIRED USING (<std::str>{});
      };
      CREATE PROPERTY subscriber: std::bool {
          SET REQUIRED USING (<std::bool>{});
      };
      CREATE PROPERTY username: std::str {
          SET REQUIRED USING (<std::str>{});
      };
      EXTENDING default::User LAST;
  };
  ALTER TYPE default::News {
      ALTER PROPERTY admin {
          RESET OPTIONALITY;
          DROP OWNED;
          RESET TYPE;
      };
      ALTER PROPERTY email {
          RESET OPTIONALITY;
          DROP OWNED;
          RESET TYPE;
      };
      ALTER PROPERTY hashed_password {
          RESET OPTIONALITY;
          DROP OWNED;
          RESET TYPE;
      };
      ALTER PROPERTY name {
          RESET OPTIONALITY;
          DROP OWNED;
          RESET TYPE;
      };
      ALTER PROPERTY subscriber {
          RESET OPTIONALITY;
          DROP OWNED;
          RESET TYPE;
      };
      ALTER PROPERTY username {
          RESET OPTIONALITY;
          DROP OWNED;
          RESET TYPE;
      };
  };
};
