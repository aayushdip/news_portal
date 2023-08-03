CREATE MIGRATION m1oukgwu2fvpaknbplv7sp76mjbyc6udr6cu2656dn52rz2cjopwgq
    ONTO m1gvavphaa53m3lax7wetipag2q3tems4wryod7bvvvlsfc7br7xoq
{
  ALTER TYPE default::News {
      DROP PROPERTY author;
  };
  ALTER TYPE default::News {
      CREATE REQUIRED LINK author: default::User {
          SET REQUIRED USING (<default::User>{});
      };
  };
};
