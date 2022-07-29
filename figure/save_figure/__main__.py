
### third-party import

from matplotlib.figure import Figure

main_callable = Figure.savefig
call_format = 'Figure.savefig'

third_party_import_text = 'from matplotlib.figure import Figure'


def _save_figure(

      figure: Figure,
      fname:'image_filepath'='.',
      *,
      format:'python_literal'=None,
      dpi: 'python_literal' = 'figure',
      metadata: dict = None,
      bbox_inches: 'python_literal'=None,
      pad_inches: 'python_literal' = 0.1,
      face_color: 'python_literal' = 'auto',
      edge_color: 'python_literal' = 'auto',
      backend: 'python_literal' = None,
      **kwargs

    ): pass

signature_callable = _save_figure
