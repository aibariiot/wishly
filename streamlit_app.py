import streamlit as st
from supabase import create_client, Client
from decimal import Decimal, InvalidOperation
from urllib.parse import urlparse
import html

st.set_page_config(
    page_title="Wishly ♡",
    page_icon="♡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Romantic theme ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600;700&family=Parisienne&display=swap');

    :root {
        --cream: #fff9f5;
        --paper: #fffdfb;
        --blush: #f7e6e6;
        --blush-deep: #e8c4ca;
        --rose: #bd7887;
        --wine: #773d50;
        --ink: #4a3038;
        --muted: #a18489;
        --line: #f0dfe0;
    }

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
        color: var(--ink);
    }

    .stApp {
        background:
          radial-gradient(ellipse at 8% 2%, rgba(247,230,230,.72), transparent 30%),
          radial-gradient(ellipse at 94% 14%, rgba(250,235,226,.72), transparent 27%),
          var(--cream);
    }

    [data-testid="stHeader"] {
        background: rgba(255,249,245,.82);
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1.2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        font-family: 'Cormorant Garamond', Georgia, serif !important;
        color: var(--ink);
    }

    h2 { font-size: 2rem !important; }
    h3 { font-size: 1.5rem !important; }

    p, label { color: var(--ink); }

    .brand {
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: 2.25rem;
        font-weight: 600;
        letter-spacing: -.055em;
        color: var(--wine);
        line-height: 1;
    }

    .brand-heart {
        color: var(--rose);
        font-size: 1.3rem;
    }

    .top-note {
        font-family: 'Parisienne', cursive;
        color: var(--rose);
        font-size: 1.45rem;
        text-align: right;
        padding-top: .15rem;
    }

    .hero {
        position: relative;
        overflow: hidden;
        background: linear-gradient(
            135deg,
            #f9e9e8 0%,
            #fff4ef 52%,
            #f5e1e3 100%
        );
        border: 1px solid #f0d8db;
        border-radius: 30px;
        padding: clamp(1.5rem, 4vw, 3.4rem);
        margin: 1.4rem 0 1.5rem;
        box-shadow: 0 14px 40px rgba(119,61,80,.06);
    }

    .hero:after {
        content: '♡';
        position: absolute;
        right: 4%;
        top: -22%;
        font-family: 'Cormorant Garamond', serif;
        font-size: 14rem;
        color: rgba(189,120,135,.12);
        transform: rotate(12deg);
        pointer-events: none;
    }

    .eyebrow {
        color: var(--rose);
        text-transform: uppercase;
        letter-spacing: .23em;
        font-size: .68rem;
        font-weight: 700;
    }

    .hero-title {
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: clamp(2.8rem, 6vw, 5.2rem);
        line-height: .94;
        letter-spacing: -.035em;
        color: var(--wine);
        margin: .7rem 0 .8rem;
        position: relative;
        z-index: 1;
    }

    .hero-script {
        font-family: 'Parisienne', cursive;
        color: var(--rose);
        font-size: clamp(1.7rem, 3vw, 2.35rem);
        margin-bottom: .7rem;
    }

    .hero-copy {
        max-width: 560px;
        color: #8f6d76;
        font-size: .95rem;
        line-height: 1.8;
    }

    .tiny-heart {
        color: var(--rose);
        letter-spacing: .28em;
        margin-top: 1rem;
    }

    [data-testid="stMetric"] {
        background: rgba(255,253,251,.78);
        border: 1px solid var(--line);
        border-radius: 20px;
        padding: 15px 18px;
        box-shadow: 0 5px 18px rgba(119,61,80,.035);
    }

    [data-testid="stMetricLabel"] {
        color: var(--muted);
    }

    [data-testid="stMetricValue"] {
        color: var(--wine);
        font-family: 'Cormorant Garamond', Georgia, serif;
    }

    div[data-testid="stTabs"] {
        margin-top: .2rem;
    }

    div[data-testid="stTabs"] [role="tablist"] {
        gap: .5rem;
        border-bottom: 1px solid var(--line);
        padding-bottom: .6rem;
    }

    div[data-testid="stTabs"] button[role="tab"] {
        border: 1px solid #f0dfe0;
        border-radius: 999px;
        background: rgba(255,253,251,.72);
        padding: .55rem 1.05rem;
        color: #956d78;
        transition: all .2s ease;
    }

    div[data-testid="stTabs"] button[aria-selected="true"] {
        background: var(--wine);
        border-color: var(--wine);
        color: white;
    }

    div[data-testid="stTabs"] button[role="tab"] p {
        color: inherit;
    }

    div.stButton > button,
    div.stFormSubmitButton > button,
    div[data-testid="stLinkButton"] a {
        border-radius: 999px;
        border: 1px solid var(--wine);
        background: var(--wine);
        color: #fffaf8;
        transition: all .2s ease;
    }

    div.stButton > button:hover,
    div.stFormSubmitButton > button:hover,
    div[data-testid="stLinkButton"] a:hover {
        background: #965d70;
        border-color: #965d70;
        color: white;
        transform: translateY(-1px);
    }

    [data-testid="stExpander"] {
        border: 1px solid var(--line);
        border-radius: 18px;
        background: rgba(255,253,251,.65);
    }

    input, textarea, [data-baseweb="select"] > div {
        border-radius: 13px !important;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255,253,251,.86);
        border-color: var(--line) !important;
        border-radius: 22px !important;
        box-shadow: 0 8px 26px rgba(119,61,80,.045);
        padding: .25rem;
        transition: transform .2s ease, box-shadow .2s ease;
    }

    [data-testid="stVerticalBlockBorderWrapper"]:hover {
        box-shadow: 0 12px 30px rgba(119,61,80,.09);
    }

    [data-testid="stImage"] img {
        border-radius: 15px;
        object-fit: cover;
    }

    .wish-category {
        text-transform: uppercase;
        letter-spacing: .18em;
        color: var(--rose);
        font-size: .66rem;
        font-weight: 700;
        margin-top: .5rem;
    }

    .wish-title {
        font-family: 'Cormorant Garamond', Georgia, serif;
        font-size: 1.55rem;
        line-height: 1.1;
        color: var(--ink);
        overflow-wrap: anywhere;
        margin: .25rem 0;
    }

    .wish-price {
        color: var(--wine);
        font-weight: 700;
        font-size: 1rem;
    }

    .empty {
        text-align: center;
        padding: 3rem 1rem;
        border: 1px dashed #e5c4cb;
        border-radius: 24px;
        background: rgba(255,253,251,.62);
    }

    .empty-heart {
        font-size: 2.4rem;
        color: var(--rose);
    }

    .empty-title {
        font-family: 'Cormorant Garamond', Georgia, serif;
        color: var(--wine);
        font-size: 2rem;
    }

    .empty-copy {
        color: var(--muted);
    }

    .section-script {
        font-family: 'Parisienne', cursive;
        color: var(--rose);
        font-size: 1.45rem;
    }

    .footer-love {
        text-align: center;
        color: #b08d96;
        font-size: .82rem;
        padding-top: 3rem;
        letter-spacing: .04em;
    }

    footer { visibility: hidden; }

    @media (max-width: 640px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero {
            border-radius: 22px;
        }

        .hero:after {
            font-size: 8rem;
            right: -2%;
            top: -8%;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- Supabase ----------
@st.cache_resource
def get_supabase() -> Client:
    url = st.secrets["SUPABASE_URL"].strip().rstrip("/")
    key = st.secrets["SUPABASE_KEY"].strip()
    return create_client(url, key)


def money(value):
    try:
        amount = Decimal(str(value or 0))
        return (
            f"{amount:,.2f} Kč"
            .replace(",", " ")
            .replace(".00 Kč", " Kč")
        )
    except (InvalidOperation, ValueError):
        return f"{value} Kč"


def valid_http_url(value):
    if not value:
        return True

    parsed = urlparse(value.strip())
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)


def load_wishes(owner):
    return (
        get_supabase()
        .table("wishes")
        .select(
            "id,owner,name,category,price,product_url,image_url,created_at"
        )
        .eq("owner", owner)
        .order("created_at", desc=True)
        .execute()
        .data
    )


def safe_text(value):
    return html.escape(str(value or ""))


# ---------- Header ----------
left, right = st.columns([2, 1])

with left:
    st.markdown(
        '<div class="brand">wishly '
        '<span class="brand-heart">♡</span></div>',
        unsafe_allow_html=True,
    )

with right:
    st.markdown(
        '<div class="top-note">made with love</div>',
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <section class="hero">
      <div class="eyebrow">A little keepsake for two hearts</div>
      <div class="hero-title">You, me<br>& all our little dreams.</div>
      <div class="hero-script">A place for everything we wish for ♡</div>
      <div class="hero-copy">
        Little things we love, beautiful things we hope for, and memories
        we cannot wait to make together. Let’s keep them here.
      </div>
      <div class="tiny-heart">♡ &nbsp; ♡ &nbsp; ♡</div>
    </section>
    """,
    unsafe_allow_html=True,
)

tab_a, tab_b, tab_c = st.tabs(
    ["♡  For Aibar", "♡  For Zhibek", "♡  Our Dreams"]
)


def render_wishlist(owner):
    try:
        wishes = load_wishes(owner)
    except Exception as exc:
        st.error(
            "Could not load wishes from Supabase. Check your project URL, API key, "
            "and that the `image_url` column exists."
        )
        st.code(str(exc))
        return

    total_value = sum(
        (Decimal(str(w.get("price") or 0)) for w in wishes),
        Decimal("0"),
    )

    st.markdown(
        '<div class="section-script">your little collection</div>',
        unsafe_allow_html=True,
    )

    metric1, metric2 = st.columns(2)
    metric1.metric("Little wishes ♡", len(wishes))
    metric2.metric("Dreams in numbers", money(total_value))

    # ---------- Add wish ----------
    with st.expander("♡  Add a little wish", expanded=False):
        with st.form(f"add_{owner}", clear_on_submit=True):
            name = st.text_input(
                "What are you dreaming of? *",
                placeholder="Something lovely…",
            )

            col1, col2 = st.columns(2)

            with col1:
                category = st.selectbox(
                    "A little category",
                    [
                        "Other",
                        "Fashion",
                        "Beauty",
                        "Tech",
                        "Home",
                        "Experiences",
                        "Travel",
                        "Books",
                        "Together",
                    ],
                )

            with col2:
                price = st.number_input(
                    "Price (Kč)",
                    min_value=0.0,
                    value=0.0,
                    step=100.0,
                    format="%.2f",
                )

            product_url = st.text_input(
                "Where can we find it? (optional)",
                placeholder="https://…",
            )

            image_url = st.text_input(
                "Photo URL (optional)",
                placeholder="https://…/photo.jpg",
            )

            submitted = st.form_submit_button(
                "Keep this wish ♡",
                use_container_width=True,
            )

            if submitted:
                if not name.strip():
                    st.warning("Add a name for your wish first ♡")

                elif not valid_http_url(product_url.strip()):
                    st.warning(
                        "The product link must start with http:// or https://."
                    )

                elif not valid_http_url(image_url.strip()):
                    st.warning(
                        "The photo URL must start with http:// or https://."
                    )

                else:
                    try:
                        get_supabase().table("wishes").insert(
                            {
                                "owner": owner,
                                "name": name.strip(),
                                "category": category,
                                "price": float(price),
                                "product_url": product_url.strip(),
                                "image_url": image_url.strip(),
                            }
                        ).execute()

                        st.success("A new little dream is saved ♡")
                        st.rerun()

                    except Exception as exc:
                        st.error(
                            "Couldn't save this wish. Check Supabase table permissions."
                        )
                        st.code(str(exc))

    st.markdown(
        '<div style="height:1px;background:#f0dfe0;margin:1.4rem 0"></div>',
        unsafe_allow_html=True,
    )

    st.subheader("Wishes to keep close")
    st.caption("Every little wish has a place here.")

    if not wishes:
        st.markdown(
            '<div class="empty">'
            '<div class="empty-heart">♡</div>'
            '<div class="empty-title">A page waiting for a dream</div>'
            '<div class="empty-copy">'
            'Add your first wish and let the little collection begin.'
            '</div>'
            '</div>',
            unsafe_allow_html=True,
        )
        return

    cols = st.columns(3, gap="medium")

    for index, wish in enumerate(wishes):
        with cols[index % 3]:
            with st.container(border=True):
                image_url = (wish.get("image_url") or "").strip()

                if image_url and valid_http_url(image_url):
                    st.image(image_url, use_container_width=True)
                else:
                    st.markdown(
                        '<div style="height:170px;border-radius:15px;'
                        'background:linear-gradient(145deg,#f9e8e8,#fff8f2 60%,#f3dfe2);'
                        'display:flex;align-items:center;justify-content:center;'
                        'color:#c78b9a;font-family:Cormorant Garamond,Georgia,serif;'
                        'font-size:3.5rem">♡</div>',
                        unsafe_allow_html=True,
                    )

                st.markdown(
                    f'<div class="wish-category">'
                    f'{safe_text(wish.get("category", "Other"))}'
                    f'</div>',
                    unsafe_allow_html=True,
                )

                st.markdown(
                    f'<div class="wish-title">'
                    f'{safe_text(wish.get("name"))}'
                    f'</div>',
                    unsafe_allow_html=True,
                )

                st.markdown(
                    f'<div class="wish-price">'
                    f'{money(wish.get("price"))} '
                    f'<span style="color:#bd7887">♡</span></div>',
                    unsafe_allow_html=True,
                )

                product_url = (wish.get("product_url") or "").strip()

                if product_url and valid_http_url(product_url):
                    st.link_button(
                        "A little look ↗",
                        product_url,
                        use_container_width=True,
                    )
                else:
                    st.caption("A wish saved with love")

                if st.button(
                    "Remove wish",
                    key=f"delete_{owner}_{wish['id']}",
                    use_container_width=True,
                ):
                    try:
                        (
                            get_supabase()
                            .table("wishes")
                            .delete()
                            .eq("id", wish["id"])
                            .eq("owner", owner)
                            .execute()
                        )
                        st.rerun()

                    except Exception as exc:
                        st.error("Couldn't remove this wish.")
                        st.code(str(exc))


with tab_a:
    render_wishlist("Aibar")

with tab_b:
    render_wishlist("Zhibek")

with tab_c:
    render_wishlist("Us")

st.markdown(
    '<div class="footer-love">'
    'You are my favourite wish. &nbsp;♡&nbsp; Always.'
    '</div>',
    unsafe_allow_html=True,
)