from django.core.validators import FileExtensionValidator


CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"

CONSTANCE_ADDITIONAL_FIELDS = {
    "image_field": [
        "django.forms.ImageField",
        {"validators": [FileExtensionValidator(allowed_extensions=["png", "jpg"])]},
    ],
}

CONSTANCE_CONFIG = {
    "LANDING_BANNER": ("none.png", "Cover Picture", "image_field"),
    "LANDING_SUBTITLE": ("De la magie dans toutes vos créations !", "Landing subtitle", str),
    "TRANSLATION_TEXT": (
        "Toutes nos équipes <b>traduisent depuis la langue d’origine</b>: japonais, chinois, coréen, anglais",
        "Translation text",
        str,
    ),
    "LETTERING_TEXT": (
        "Nous <b>maitrisons Photoshop et Indesign</b> pour intégrer le texte traduit dans vos séries",
        "Lettering text",
        str,
    ),
    "CORRECTION_TEXT": (
        "Nous <b>corrigeons</b> et <b>adaptons</b> toutes les traductions pour les rendre les plus fluides et \
            agréables possible",
        "Correction text",
        str,
    ),
    "GRAPHISM_TEXT": (
        "Nous <b>reconstruisons toutes les images</b> après avoir effacé les textes d’origines et réalisons <b>le \
            montage des maquettes</b>",
        "Graphism text",
        str,
    ),
    "EDITION_TEXT": (
        "Nous faisons en sorte que <b>tous les acteurs remplissent leur rôle à la perfection</b>",
        "Edition text",
        str,
    ),
    "STUDIO_FIRST_PARAGRAPH": (
        'Bienvenue au Studio Magi, votre partenaire de confiance pour la localisation de contenus manga, manhua, \
            webtoon et light novel. Fondé en février 2022 par les éditions ManED avec pour objectif de dynamiser une \
                équipe sous-staffée, notre studio a rapidement pris son envol en offrant des services de qualité à nos \
                    premiers partenaires, notamment Izneo (aujourd\'hui Ono), avec qui nous avons collaboré sur des \
                        séries telles que "She may not be cute", "Straight F witch" et \
                            "The best like the sunlight".',
        "Studio section first paragraph",
        str,
    ),
    "STUDIO_SECOND_PARAGRAPH": (
        "Depuis nos débuts, nous avons élargi notre portefeuille de clients et de partenaires, rencontrant de nouveaux \
            acteurs passionnants lors de Japan Expo 2022. Cette rencontre a marqué le début de collaborations \
                fructueuses avec des plateformes et éditeurs telles que Piccoma, Nazca Editions et Mangas.io. En \
                    janvier 2023, nous avons consolidé notre présence sur le marché par le rachat de la société ManED \
                        au sein de Mahô éditions, renforçant ainsi notre position dans le domaine de la localisation.",
        "Studio section second paragraph",
        str,
    ),
    "STUDIO_THIRD_PARAGRAPH": (
        "Nos efforts continus pour offrir des services de qualité supérieure nous ont permis d'attirer de nouveaux \
            clients prestigieux tout au long de l'année 2023, parmi lesquels figurent Naban, Hariken, Taicca, \
                Blackbox, JNC Nina, et bien d'autres encore. Nous sommes fiers de jouer un rôle essentiel dans la mise \
                    en valeur de leurs contenus auprès du public francophone.",
        "Studio section third paragraph",
        str,
    ),
    "STUDIO_FOURTH_PARAGRAPH": (
        "Notre équipe dévouée est composée de professionnels chevronnés, comprenant 1 directeur de projet, 5 éditeurs, \
            2 managers, 12 lettreurs, 11 traducteurs japonais, 2 traducteurs chinois, 14 traducteurs coréens, 8 \
                correcteurs, 4 reconstructeurs et 6 relecteurs. Chaque membre apporte son expertise unique pour \
                    garantir des résultats exceptionnels à chaque projet.",
        "Studio section fourth paragraph",
        str,
    ),
    "STUDIO_FIFTH_PARAGRAPH": (
        "Au Studio Magi, nous sommes animés par notre passion pour les médias visuels et notre engagement envers \
            l'excellence. Nous sommes impatients de collaborer avec vous et de vous aider à donner vie à vos projets \
                les plus ambitieux.",
        "Studio section fifth paragraph",
        str,
    ),
    "STUDIO_BOTTOM_TEXT": (
        "Contactez-nous dès aujourd'hui pour discuter de la manière dont nous pouvons vous accompagner dans la \
            réalisation de vos besoins de localisation.",
        "Studio section bottom text",
        str,
    ),
    "CONTACT_CONTENT": (
        """<p>
    Si vous souhaitez nous confier un projet, obtenir un devis ou toute autre demande, contactez-nous :
</p>
<p>
    <b>Hicham Chennaf</b>
    <a class = "bi bi-at text-primary d-block" href = "mailto:hicham.chennaf@maho-editions.fr?subject=Magi Studio \
        Contact">&nbsp;hicham.chennaf@maho-editions.fr</a>
    <a class = "bi bi-telephone text-primary d-block" href = "href=tel:+33681158383">&nbsp;06 81 15 83 83</a>
</p>
<p>
    Pour toutes les demandes de recrutements, ce dernier ne se fait que par co-optation. Ne nous contactez donc pas à \
        ce sujet via cette fiche de contact.
</p>
<p>
    Cette solution a été adopté par le studio afin de conserver une équipe de confiance et de qualité.
        </p>""",
        "Contact HTML content",
        str,
    ),
}

CONSTANCE_CONFIG_FIELDSETS = {
    "Landing": (
        "LANDING_BANNER",
        "LANDING_SUBTITLE",
        "TRANSLATION_TEXT",
        "LETTERING_TEXT",
        "CORRECTION_TEXT",
        "GRAPHISM_TEXT",
        "EDITION_TEXT",
    ),
    "Studio": (
        "STUDIO_FIRST_PARAGRAPH",
        "STUDIO_SECOND_PARAGRAPH",
        "STUDIO_THIRD_PARAGRAPH",
        "STUDIO_FOURTH_PARAGRAPH",
        "STUDIO_FIFTH_PARAGRAPH",
        "STUDIO_BOTTOM_TEXT",
    ),
    "Contact": ("CONTACT_CONTENT",),
}
