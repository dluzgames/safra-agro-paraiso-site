import base64
import os
from pathlib import Path

# Paths
ASSETS_DIR = Path(r"c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard\sites\safra-agro-paraiso\assets")
CRIATIVOS_DIR = ASSETS_DIR / "criativos"
CRIATIVOS_DIR.mkdir(parents=True, exist_ok=True)

def b64_img(path: Path) -> str:
    ext = path.suffix.lower()
    mime = "image/png" if ext == ".png" else "image/jpeg"
    data = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{data}"

logo_b64 = b64_img(ASSETS_DIR / "logo.jpg")
sorgo_b64 = b64_img(ASSETS_DIR / "sorgo_clean.jpg")
casquinha_b64 = b64_img(ASSETS_DIR / "casquinha_clean.jpg")

# Colors - White Theme
BRAND_PRIMARY = "#0F6D38"
BRAND_LIGHT = "#158A48"
BRAND_DARK = "#094723"
GOLD = "#C2851B"
GOLD_LIGHT = "#E0A838"
GOLD_BG = "#FDF8EE"
GOLD_BORDER = "#F0DFC0"

WHITE_BG = "#FFFFFF"
CARD_BG = "#F8FAF7"
CARD_BORDER = "#E2EAE0"
TEXT_DARK = "#0B2315"
TEXT_MUTED = "#4A6353"
TEXT_LIGHT = "#718779"

TOTAL_SLIDES = 5

def progress_bar(idx: int) -> str:
    pct = ((idx + 1) / TOTAL_SLIDES) * 100
    track = "rgba(0,0,0,0.06)"
    fill = BRAND_PRIMARY
    label_color = "rgba(0,0,0,0.38)"
    return f"""
    <div style="position:absolute;bottom:0;left:0;right:0;padding:12px 28px 16px;z-index:20;display:flex;align-items:center;gap:10px;">
        <div style="flex:1;height:3px;background:{track};border-radius:2px;overflow:hidden;">
            <div style="height:100%;width:{pct}%;background:{fill};border-radius:2px;"></div>
        </div>
        <span style="font-size:11px;color:{label_color};font-weight:700;font-family:'Plus Jakarta Sans',sans-serif;">{idx + 1}/{TOTAL_SLIDES}</span>
    </div>
    """

def swipe_arrow() -> str:
    bg = "rgba(0,0,0,0.04)"
    stroke = "rgba(0,0,0,0.25)"
    return f"""
    <div style="position:absolute;right:0;top:0;bottom:0;width:38px;z-index:15;display:flex;align-items:center;justify-content:center;background:linear-gradient(to right,transparent,{bg});pointer-events:none;">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
            <path d="M9 6l6 6-6 6" stroke="{stroke}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
    </div>
    """

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carrossel Safra Agro - Fundo Branco</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-font-smoothing: antialiased;
        }}
        body {{
            background: #E8ECE9;
            color: {TEXT_DARK};
            font-family: 'Plus Jakarta Sans', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }}
        .ig-frame {{
            width: 420px;
            background: #fff;
            border-radius: 20px;
            overflow: hidden;
            box-shadow: 0 25px 50px -12px rgba(0,0,0,0.15);
            border: 1px solid #DDE3DC;
        }}
        .ig-header {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px 16px;
            background: #FAFCFA;
            border-bottom: 1px solid #E8EFE6;
        }}
        .ig-user {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .ig-avatar {{
            width: 34px;
            height: 34px;
            border-radius: 50%;
            border: 1.5px solid {BRAND_PRIMARY};
            overflow: hidden;
            background: #fff;
        }}
        .ig-avatar img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
        }}
        .ig-username {{
            font-size: 13px;
            font-weight: 700;
            color: {TEXT_DARK};
        }}
        .ig-location {{
            font-size: 10px;
            color: {TEXT_LIGHT};
        }}
        .carousel-viewport {{
            width: 420px;
            height: 525px;
            overflow: hidden;
            position: relative;
        }}
        .carousel-track {{
            display: flex;
            width: {420 * TOTAL_SLIDES}px;
            height: 100%;
            transition: transform 0.3s cubic-bezier(0.2, 0, 0.2, 1);
        }}
        .slide {{
            width: 420px;
            height: 525px;
            position: relative;
            flex-shrink: 0;
            overflow: hidden;
            padding: 24px 28px 48px;
            display: flex;
            flex-direction: column;
            background: {WHITE_BG};
            color: {TEXT_DARK};
        }}

        /* Typography & Components */
        .tag-pill {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 0.8px;
            text-transform: uppercase;
            width: fit-content;
        }}
    </style>
</head>
<body>

<div class="ig-frame">
    <!-- IG Header -->
    <div class="ig-header">
        <div class="ig-user">
            <div class="ig-avatar">
                <img src="{logo_b64}" alt="Safra Agro">
            </div>
            <div>
                <div class="ig-username">safraagro_paraiso</div>
                <div class="ig-location">Paraíso do Tocantins - TO</div>
            </div>
        </div>
        <div style="color:#888;font-size:18px;">•••</div>
    </div>

    <!-- Carousel Viewport -->
    <div class="carousel-viewport">
        <div class="carousel-track">

            <!-- ================= SLIDE 1: HOOK (WHITE BG) ================= -->
            <div class="slide">
                {swipe_arrow()}
                {progress_bar(0)}

                <!-- Top bar -->
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
                    <span class="tag-pill" style="background:rgba(15,109,56,0.08);color:{BRAND_PRIMARY};border:1px solid rgba(15,109,56,0.2);">
                        NUTRIÇÃO BOVINA • TO
                    </span>
                    <div style="display:flex;align-items:center;gap:6px;">
                        <img src="{logo_b64}" style="width:22px;height:22px;border-radius:4px;object-fit:contain;">
                        <span style="font-size:11px;font-weight:700;color:{BRAND_PRIMARY};">SAFRA AGRO</span>
                    </div>
                </div>

                <!-- Main Hook Title -->
                <div style="margin-bottom:14px;">
                    <h1 style="font-size:26px;font-weight:900;line-height:1.15;color:{TEXT_DARK};letter-spacing:-0.5px;">
                        SORGO OU CASQUINHA DE SOJA?
                    </h1>
                    <p style="font-size:13px;font-weight:600;color:{TEXT_MUTED};margin-top:4px;line-height:1.35;">
                        Qual gera <span style="color:{BRAND_PRIMARY};font-weight:800;background:rgba(15,109,56,0.08);padding:1px 5px;border-radius:4px;">mais arrobas</span> pelo menor custo na nutrição do seu gado?
                    </p>
                </div>

                <!-- Split Comparison Visual (Real Photos) -->
                <div style="display:flex;gap:10px;margin-bottom:14px;position:relative;">
                    <!-- Sorgo Card -->
                    <div style="flex:1;background:#fff;border:1px solid {CARD_BORDER};border-radius:12px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,0.04);">
                        <div style="height:100px;overflow:hidden;position:relative;">
                            <img src="{sorgo_b64}" style="width:100%;height:100%;object-fit:cover;">
                            <span style="position:absolute;top:6px;left:6px;background:rgba(0,0,0,0.65);color:#fff;font-size:9px;font-weight:700;padding:2px 6px;border-radius:4px;">ENERGIA</span>
                        </div>
                        <div style="padding:8px 10px;">
                            <div style="font-size:12px;font-weight:800;color:{TEXT_DARK};">Sorgo em Grãos</div>
                            <div style="font-size:10px;color:{TEXT_LIGHT};margin-top:2px;">Substituto do milho</div>
                        </div>
                    </div>

                    <!-- VS Badge -->
                    <div style="position:absolute;top:45px;left:50%;transform:translate(-50%,-50%);z-index:5;background:{GOLD_LIGHT};color:#000;font-size:11px;font-weight:900;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 2px 8px rgba(0,0,0,0.15);border:2px solid #fff;">
                        VS
                    </div>

                    <!-- Casquinha Card -->
                    <div style="flex:1;background:#fff;border:1px solid {CARD_BORDER};border-radius:12px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,0.04);">
                        <div style="height:100px;overflow:hidden;position:relative;">
                            <img src="{casquinha_b64}" style="width:100%;height:100%;object-fit:cover;">
                            <span style="position:absolute;top:6px;left:6px;background:{BRAND_PRIMARY};color:#fff;font-size:9px;font-weight:700;padding:2px 6px;border-radius:4px;">FIBRA NOBRE</span>
                        </div>
                        <div style="padding:8px 10px;">
                            <div style="font-size:12px;font-weight:800;color:{TEXT_DARK};">Casquinha de Soja</div>
                            <div style="font-size:10px;color:{TEXT_LIGHT};margin-top:2px;">Alto NDT ruminal</div>
                        </div>
                    </div>
                </div>

                <!-- Benefit Pill / Hook Footer -->
                <div style="background:{CARD_BG};border-left:4px solid {BRAND_PRIMARY};border:1px solid {CARD_BORDER};padding:10px 12px;border-radius:0 8px 8px 0;">
                    <div style="font-size:11px;font-weight:700;color:{BRAND_PRIMARY};">DECISÃO ESTRATÉGICA NO COCHO:</div>
                    <div style="font-size:11px;color:{TEXT_MUTED};line-height:1.35;margin-top:2px;">
                        Descubra a diferença prática de cada alimento e a combinação campeã dos maiores pecuaristas.
                    </div>
                </div>

                <div style="margin-top:auto;display:flex;align-items:center;justify-content:space-between;padding-top:6px;">
                    <span style="font-size:10px;color:{TEXT_LIGHT};font-weight:600;">Arraste para comparar 👉</span>
                    <span style="font-size:10px;color:{BRAND_PRIMARY};font-weight:700;">@safraagro_paraiso</span>
                </div>
            </div>

            <!-- ================= SLIDE 2: SORGO (WHITE BG) ================= -->
            <div class="slide">
                {swipe_arrow()}
                {progress_bar(1)}

                <!-- Top bar -->
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
                    <span class="tag-pill" style="background:{GOLD_BG};color:{GOLD};border:1px solid {GOLD_BORDER};">
                        01 • FONTE ENERGÉTICA
                    </span>
                    <span style="font-size:10px;color:{TEXT_LIGHT};font-weight:600;">ALTO RENDIMENTO</span>
                </div>

                <!-- Title -->
                <h2 style="font-size:22px;font-weight:800;line-height:1.2;color:{TEXT_DARK};margin-bottom:10px;">
                    Sorgo em Grãos: <br><span style="color:{GOLD};">A Potência do Amido</span>
                </h2>

                <!-- Product Hero Card with Real Image -->
                <div style="background:{CARD_BG};border:1px solid {CARD_BORDER};border-radius:12px;overflow:hidden;margin-bottom:12px;display:flex;align-items:center;box-shadow:0 3px 10px rgba(0,0,0,0.03);">
                    <div style="width:110px;height:84px;flex-shrink:0;overflow:hidden;">
                        <img src="{sorgo_b64}" style="width:100%;height:100%;object-fit:cover;">
                    </div>
                    <div style="padding:10px 12px;">
                        <div style="font-size:12px;font-weight:800;color:{GOLD};">Grãos Selecionados Safra Agro</div>
                        <div style="font-size:10px;color:{TEXT_MUTED};margin-top:2px;line-height:1.3;">
                            Rico em amido de excelente fermentação para ganho de peso acelerado.
                        </div>
                    </div>
                </div>

                <!-- 3 Key Highlights -->
                <div style="display:flex;flex-direction:column;gap:8px;">
                    <div style="display:flex;align-items:flex-start;gap:10px;background:{CARD_BG};border:1px solid {CARD_BORDER};padding:8px 10px;border-radius:8px;">
                        <div style="background:{GOLD};color:#fff;font-weight:900;font-size:10px;padding:2px 6px;border-radius:4px;margin-top:2px;">ECO</div>
                        <div style="font-size:11px;line-height:1.35;color:{TEXT_DARK};">
                            <strong style="color:{GOLD};">Custo até 25% menor que o milho</strong> mantendo entre 85% e 95% do mesmo valor energético.
                        </div>
                    </div>

                    <div style="display:flex;align-items:flex-start;gap:10px;background:{CARD_BG};border:1px solid {CARD_BORDER};padding:8px 10px;border-radius:8px;">
                        <div style="background:{GOLD};color:#fff;font-weight:900;font-size:10px;padding:2px 6px;border-radius:4px;margin-top:2px;">GMD</div>
                        <div style="font-size:11px;line-height:1.35;color:{TEXT_DARK};">
                            <strong style="color:{GOLD};">Acabamento de carcaça rápido:</strong> amido denso que acelera a deposição de gordura na fase final.
                        </div>
                    </div>

                    <div style="display:flex;align-items:flex-start;gap:10px;background:{CARD_BG};border:1px solid {CARD_BORDER};padding:8px 10px;border-radius:8px;">
                        <div style="background:{GOLD};color:#fff;font-weight:900;font-size:10px;padding:2px 6px;border-radius:4px;margin-top:2px;">USO</div>
                        <div style="font-size:11px;line-height:1.35;color:{TEXT_DARK};">
                            <strong style="color:{GOLD};">Versátil:</strong> ideal para confinamento, semiconfinamento e ração concentrada de corte e leite.
                        </div>
                    </div>
                </div>

                <div style="margin-top:auto;font-size:10px;color:{TEXT_LIGHT};display:flex;justify-content:space-between;">
                    <span>Próximo: Casquinha de Soja</span>
                    <span>Deslize 👉</span>
                </div>
            </div>

            <!-- ================= SLIDE 3: CASQUINHA (WHITE BG) ================= -->
            <div class="slide">
                {swipe_arrow()}
                {progress_bar(2)}

                <!-- Top bar -->
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
                    <span class="tag-pill" style="background:rgba(15,109,56,0.08);color:{BRAND_PRIMARY};border:1px solid rgba(15,109,56,0.25);">
                        02 • FIBRA DIGESTÍVEL
                    </span>
                    <span style="font-size:10px;color:{TEXT_LIGHT};font-weight:600;">SEGURANÇA RUMINAL</span>
                </div>

                <!-- Title -->
                <h2 style="font-size:22px;font-weight:800;line-height:1.2;color:{TEXT_DARK};margin-bottom:10px;">
                    Casquinha de Soja: <br><span style="color:{BRAND_PRIMARY};">Energia sem Risco de Acidose</span>
                </h2>

                <!-- Product Hero Card with Real Image -->
                <div style="background:{CARD_BG};border:1px solid {CARD_BORDER};border-radius:12px;overflow:hidden;margin-bottom:12px;display:flex;align-items:center;box-shadow:0 3px 10px rgba(0,0,0,0.03);">
                    <div style="width:110px;height:84px;flex-shrink:0;overflow:hidden;">
                        <img src="{casquinha_b64}" style="width:100%;height:100%;object-fit:cover;">
                    </div>
                    <div style="padding:10px 12px;">
                        <div style="font-size:12px;font-weight:800;color:{BRAND_PRIMARY};">Pelletizada Padrão Safra Agro</div>
                        <div style="font-size:10px;color:{TEXT_MUTED};margin-top:2px;line-height:1.3;">
                            Excelente palatabilidade e uniformidade para misturadores e cochos.
                        </div>
                    </div>
                </div>

                <!-- 3 Key Highlights -->
                <div style="display:flex;flex-direction:column;gap:8px;">
                    <div style="display:flex;align-items:flex-start;gap:10px;background:{CARD_BG};border:1px solid {CARD_BORDER};padding:8px 10px;border-radius:8px;">
                        <div style="background:{BRAND_PRIMARY};color:#fff;font-weight:900;font-size:10px;padding:2px 6px;border-radius:4px;margin-top:2px;">NDT</div>
                        <div style="font-size:11px;line-height:1.35;color:{TEXT_DARK};">
                            <strong style="color:{BRAND_PRIMARY};">NDT elevado (~75% a 80%):</strong> fornece energia comparável aos grãos, mas via pectina e fibra solúvel.
                        </div>
                    </div>

                    <div style="display:flex;align-items:flex-start;gap:10px;background:{CARD_BG};border:1px solid {CARD_BORDER};padding:8px 10px;border-radius:8px;">
                        <div style="background:{BRAND_PRIMARY};color:#fff;font-weight:900;font-size:10px;padding:2px 6px;border-radius:4px;margin-top:2px;">RÚMEN</div>
                        <div style="font-size:11px;line-height:1.35;color:{TEXT_DARK};">
                            <strong style="color:{BRAND_PRIMARY};">Protege o rúmen:</strong> não causa queda brusca de pH, estimulando a digestão do capim e volumoso seco.
                        </div>
                    </div>

                    <div style="display:flex;align-items:flex-start;gap:10px;background:{CARD_BG};border:1px solid {CARD_BORDER};padding:8px 10px;border-radius:8px;">
                        <div style="background:{BRAND_PRIMARY};color:#fff;font-weight:900;font-size:10px;padding:2px 6px;border-radius:4px;margin-top:2px;">PELLET</div>
                        <div style="font-size:11px;line-height:1.35;color:{TEXT_DARK};">
                            <strong style="color:{BRAND_PRIMARY};">Zero desperdício:</strong> forma pelletizada evita perda por vento no cocho e facilita a homogeneização.
                        </div>
                    </div>
                </div>

                <div style="margin-top:auto;font-size:10px;color:{TEXT_LIGHT};display:flex;justify-content:space-between;">
                    <span>Próximo: A Combinação Ideal</span>
                    <span>Deslize 👉</span>
                </div>
            </div>

            <!-- ================= SLIDE 4: VEREDICTO / SÍNTESE (WHITE BG) ================= -->
            <div class="slide">
                {swipe_arrow()}
                {progress_bar(3)}

                <!-- Top bar -->
                <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;">
                    <span class="tag-pill" style="background:{GOLD_BG};color:{GOLD};border:1px solid {GOLD_BORDER};">
                        ESTRATÉGIA DE OURO
                    </span>
                    <span style="font-size:10px;color:{BRAND_PRIMARY};font-weight:700;">MÁXIMA EFICIÊNCIA</span>
                </div>

                <!-- Title -->
                <h2 style="font-size:22px;font-weight:900;line-height:1.2;color:{TEXT_DARK};margin-bottom:12px;">
                    Por que escolher um <br>se você pode <span style="color:{BRAND_PRIMARY};">associar os dois?</span>
                </h2>

                <!-- Synergy Concept Card -->
                <div style="background:rgba(15,109,56,0.06);border:1px solid rgba(15,109,56,0.18);border-radius:12px;padding:12px 14px;margin-bottom:12px;">
                    <p style="font-size:11px;line-height:1.45;color:{TEXT_DARK};">
                        💡 <strong style="color:{BRAND_PRIMARY};">A Fórmula do Confinamento Inteligente:</strong><br>
                        Enquanto o <strong>Sorgo</strong> entrega o pico de amido necessário para engordar e finalizar, a <strong>Casquinha</strong> dá sustentação ruminal para o animal comer mais sem travar o rúmen.
                    </p>
                </div>

                <!-- Comparison Table Matrix -->
                <div style="background:#fff;border-radius:10px;overflow:hidden;border:1px solid {CARD_BORDER};margin-bottom:12px;box-shadow:0 2px 8px rgba(0,0,0,0.03);">
                    <div style="display:flex;background:#EDF4EC;padding:7px 10px;font-size:10px;font-weight:800;color:{BRAND_PRIMARY};border-bottom:1px solid {CARD_BORDER};">
                        <div style="flex:1.2;">ALIMENTO</div>
                        <div style="flex:1.5;">PAPEL NA DIETA</div>
                        <div style="flex:1.3;text-align:right;">RESULTADO</div>
                    </div>
                    <div style="display:flex;padding:8px 10px;font-size:10.5px;border-bottom:1px solid {CARD_BORDER};align-items:center;">
                        <div style="flex:1.2;font-weight:800;color:{TEXT_DARK};">🌾 Sorgo</div>
                        <div style="flex:1.5;color:{TEXT_MUTED};">Amido & Energia rápida</div>
                        <div style="flex:1.3;text-align:right;color:{GOLD};font-weight:800;">+ Gordura / GMD</div>
                    </div>
                    <div style="display:flex;padding:8px 10px;font-size:10.5px;align-items:center;">
                        <div style="flex:1.2;font-weight:800;color:{TEXT_DARK};">🌱 Casquinha</div>
                        <div style="flex:1.5;color:{TEXT_MUTED};">Fibra nobre & NDT</div>
                        <div style="flex:1.3;text-align:right;color:{BRAND_PRIMARY};font-weight:800;">+ Digestão / Rúmen</div>
                    </div>
                </div>

                <!-- Key Takeaway -->
                <div style="background:{GOLD_BG};border:1px solid {GOLD_BORDER};border-radius:8px;padding:9px 12px;text-align:center;">
                    <span style="font-size:11px;font-weight:800;color:{GOLD};">
                        Resultado: Menor custo por arroba e máxima conversão alimentar.
                    </span>
                </div>

                <div style="margin-top:auto;font-size:10px;color:{TEXT_LIGHT};display:flex;justify-content:space-between;">
                    <span>Último: Como Comprar em TO</span>
                    <span>Deslize 👉</span>
                </div>
            </div>

            <!-- ================= SLIDE 5: CTA COMERCIAL (WHITE BG) ================= -->
            <div class="slide" style="justify-content:center;text-align:center;">
                {progress_bar(4)}

                <div style="display:flex;flex-direction:column;align-items:center;">
                    <!-- Top Logo Badge -->
                    <div style="margin:0 auto 10px;width:58px;height:58px;border-radius:50%;background:#fff;border:2px solid {BRAND_PRIMARY};display:flex;align-items:center;justify-content:center;overflow:hidden;box-shadow:0 4px 14px rgba(15,109,56,0.15);">
                        <img src="{logo_b64}" style="width:46px;height:46px;object-fit:contain;">
                    </div>

                    <span class="tag-pill" style="margin:0 auto 10px;background:rgba(15,109,56,0.08);color:{BRAND_PRIMARY};border:1px solid rgba(15,109,56,0.25);">
                        PRONTA-ENTREGA NO TOCANTINS
                    </span>

                    <h2 style="font-size:23px;font-weight:900;line-height:1.2;color:{TEXT_DARK};margin-bottom:6px;">
                        Garanta seu Lote com <br><span style="color:{BRAND_PRIMARY};">Preço Direto de Carga</span>
                    </h2>

                    <p style="font-size:11px;color:{TEXT_MUTED};max-width:320px;margin:0 auto 14px;line-height:1.35;">
                        Nutrição de alta performance para o seu rebanho com carregamento imediato em <strong>Paraíso do Tocantins - TO</strong>.
                    </p>

                    <!-- 3 Badges de Confiança -->
                    <div style="display:flex;justify-content:center;gap:6px;margin-bottom:16px;width:100%;">
                        <div style="background:{CARD_BG};border:1px solid {CARD_BORDER};padding:7px 8px;border-radius:8px;font-size:10px;flex:1;color:{TEXT_DARK};box-shadow:0 2px 6px rgba(0,0,0,0.02);">
                            📦 <strong>Sacaria & Big Bag</strong>
                        </div>
                        <div style="background:{CARD_BG};border:1px solid {CARD_BORDER};padding:7px 8px;border-radius:8px;font-size:10px;flex:1;color:{TEXT_DARK};box-shadow:0 2px 6px rgba(0,0,0,0.02);">
                            ⚡ <strong>Carregamento Rápido</strong>
                        </div>
                        <div style="background:{CARD_BG};border:1px solid {CARD_BORDER};padding:7px 8px;border-radius:8px;font-size:10px;flex:1;color:{TEXT_DARK};box-shadow:0 2px 6px rgba(0,0,0,0.02);">
                            🌾 <strong>Grãos Selecionados</strong>
                        </div>
                    </div>

                    <!-- CTA Button Box -->
                    <div style="background:linear-gradient(135deg, {BRAND_PRIMARY} 0%, #158A48 100%);color:#FFFFFF;padding:12px 24px;border-radius:30px;font-weight:900;font-size:13px;display:inline-flex;align-items:center;justify-content:center;gap:8px;box-shadow:0 8px 24px rgba(15,109,56,0.28);margin-bottom:12px;letter-spacing:0.3px;">
                        <span>📲 COTAR SACA OU TONELADA</span>
                    </div>

                    <!-- Direct Contact Info -->
                    <div style="font-size:13px;font-weight:800;color:{TEXT_DARK};margin-bottom:2px;">
                        WhatsApp: <span style="color:{BRAND_PRIMARY}; font-weight:900;">(63) 99219-8016</span>
                    </div>
                    <div style="font-size:10px;color:{TEXT_LIGHT};">
                        Instagram: <strong style="color:{BRAND_PRIMARY};">@safraagro_paraiso</strong> • Paraíso do Tocantins
                    </div>
                </div>
            </div>

        </div>
    </div>
</div>

</body>
</html>
"""

html_path = CRIATIVOS_DIR / "carousel.html"
html_path.write_text(html_content, encoding="utf-8")
print(f"HTML updated with white theme successfully at: {html_path}")
