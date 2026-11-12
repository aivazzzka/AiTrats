// AiTrats Supabase configuration
// Frontend initializes @supabase/supabase-js (CDN) in index.html and saves user data
// by unique telegram_id in the `user_finances` table.

export const SUPABASE_URL = "https://jpspzhhksyqffkjrddya.supabase.co";
export const SUPABASE_PUBLISHABLE_KEY = "sb_publishable_3zAuHGjU4taZ3JyvhNFcYg_xdyIq97V";
export const USER_FINANCES_TABLE = "user_finances";
export const USER_ID_COLUMN = "telegram_id";

// Example client initialization (for module/bundler environments):
// import { createClient } from "@supabase/supabase-js";
// export const supabase = createClient(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY, {
//   auth: { persistSession: false, autoRefreshToken: false, detectSessionInUrl: false }
// });