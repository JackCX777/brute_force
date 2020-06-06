import server_settings
import substitution_password_attacks
import brute_force_password_attacks
import attack_plans


# attack_plans.smart_password_attack(
#     substitution_password_attacks.brute_by_target_info,
#     substitution_password_attacks.brute_by_password_list,
#     brute_force_password_attacks.brute_force_password
# )

# attack_plans.password_attack_by_target_info_only(substitution_password_attacks.brute_by_target_info)

# attack_plans.password_attack_by_common_list_only(substitution_password_attacks.brute_by_password_list)

attack_plans.password_attack_by_brute_force_only(brute_force_password_attacks.brute_force_password)
