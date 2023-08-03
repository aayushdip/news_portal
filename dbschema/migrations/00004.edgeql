CREATE MIGRATION m15r53xfc3idyaveld5nkl6azrato3guth6nzxgtlrtjfj6hlrgniq
    ONTO m1oukgwu2fvpaknbplv7sp76mjbyc6udr6cu2656dn52rz2cjopwgq
{
  ALTER TYPE default::News DROP EXTENDING default::User;
};
