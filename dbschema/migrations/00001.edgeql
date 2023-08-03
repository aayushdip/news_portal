CREATE MIGRATION m12xjv24iyhrmd3eqnir2e3kxgsi62o6z6kuiofboag356zuqayi4a
    ONTO initial
{
  CREATE TYPE default::Company {
      CREATE REQUIRED PROPERTY contact_no: std::str;
      CREATE REQUIRED PROPERTY country: std::str;
      CREATE REQUIRED PROPERTY email: std::str {
          CREATE CONSTRAINT std::regexp(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$');
      };
      CREATE REQUIRED PROPERTY founded_date: cal::local_date;
      CREATE REQUIRED PROPERTY name: std::str;
      CREATE REQUIRED PROPERTY website: std::str;
  };
  CREATE TYPE default::News {
      CREATE REQUIRED PROPERTY author: std::str;
      CREATE REQUIRED PROPERTY country: std::str;
      CREATE REQUIRED PROPERTY date_published: cal::local_date;
      CREATE REQUIRED PROPERTY news_content: std::str;
      CREATE REQUIRED PROPERTY section: std::str;
      CREATE REQUIRED PROPERTY title: std::str;
  };
  CREATE TYPE default::User {
      CREATE REQUIRED PROPERTY admin: std::bool;
      CREATE REQUIRED PROPERTY email: std::str {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE REQUIRED PROPERTY hashed_password: std::str;
      CREATE REQUIRED PROPERTY name: std::str;
      CREATE REQUIRED PROPERTY subscriber: std::bool;
      CREATE REQUIRED PROPERTY username: std::str {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
