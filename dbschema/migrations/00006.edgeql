CREATE MIGRATION m12nzdcp43ovo6t6fxbq6u3dpdhmg3g5ugdkqztrcdix3zob7lkmtq
    ONTO m1ngxhoayr5s634zze3cyokd7tmhzhgzloaeq6ooz6qowzulbcl2ya
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
