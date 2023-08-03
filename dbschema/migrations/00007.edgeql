CREATE MIGRATION m1k5kycleusgqjihfxcureupydou6fjrde3awjkelkrzlkdvi6fika
    ONTO m12nzdcp43ovo6t6fxbq6u3dpdhmg3g5ugdkqztrcdix3zob7lkmtq
{
  ALTER TYPE default::News DROP EXTENDING default::User;
};
