CREATE MIGRATION m1ltthapbahhhbpk2mcm7ofuckhr7szm6uoevimcobtmyno2hukvra
    ONTO m1j4ya3ob6iz2d3o26taphgrzn3sbh6b6hkgxxfvofyy7vooyol2la
{
  ALTER TYPE default::News {
      CREATE REQUIRED PROPERTY news_content: std::str {
          SET REQUIRED USING (<std::str>{});
      };
  };
};
