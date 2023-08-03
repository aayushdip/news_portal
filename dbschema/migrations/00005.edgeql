CREATE MIGRATION m1ngxhoayr5s634zze3cyokd7tmhzhgzloaeq6ooz6qowzulbcl2ya
    ONTO m15r53xfc3idyaveld5nkl6azrato3guth6nzxgtlrtjfj6hlrgniq
{
  ALTER TYPE default::News {
      ALTER LINK author {
          RESET OPTIONALITY;
      };
  };
};
