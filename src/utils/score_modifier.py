def modify_sim_score_of_name(sim_score, target_name,magic_numbers):
  """
  This will modify the similarity score based on magic numbers to make the statistical model more robust

  Args:
  target_name (str): The name of the target column
  sim_score(float): similarity score
  magic_numbers(dict) = magic numbers in form of dictionary

  returns:
  sim_score: The modified similarity score
  need_to_continue(bool): Stating that whether we need to calculate the similarity score from values or not
  """

  # Setting Default value of need to continue to True
  need_to_continue = True

  # For Clarity
  if target_name == "clarity":

    if sim_score > magic_numbers['clarity_threshold']:
      need_to_continue = False
    else:
      sim_score = (sim_score * magic_numbers['clarity_normalizing_factor_for_col_name'])
    
  # For Carat
  elif target_name == "carat":
    sim_score *= magic_numbers['carat_normalizing_factor_for_col_name']

  # For Color
  elif target_name == "color":

    if sim_score > magic_numbers['color_threshold']:
      need_to_continue = False
    else:
      sim_score *= magic_numbers['color_normalizing_factor_for_col_name']
  
  # For shape (Modification Remaining and will be done in future)
  elif target_name == "shape":
      pass
  
  # For fluorescent
  elif target_name == "fluorescent":
    if sim_score > magic_numbers['fluor_similarity_threshold']:
      need_to_continue = True
    else:
      sim_score *= magic_numbers['fluor_normalizing_factor_for_col_name']
  
  # For raprate
  elif target_name == "raprate":
    if sim_score >= magic_numbers['raprate_threshold_factor']:
      need_to_continue = False
    else:
      sim_score *= magic_numbers['raprate_normalizing_factor_for_col_name']
  
  elif target_name in ["length","width","depth"]:
    sim_score = sim_score * magic_numbers['measurement_normalizing_factor_for_col_name']
  
  #For Cut
  elif target_name == "cut":
    if sim_score > magic_numbers['cut_similarity_threshold']:
      need_to_continue = True
    else:
      sim_score *= magic_numbers['cut_normalizing_factor_for_col_name']
  
  #For Polish
  elif target_name == "polish":
    if sim_score > magic_numbers['polish_similarity_threshold']:
      need_to_continue = True
    else:
      sim_score *= magic_numbers['polish_normalizing_factor_for_col_name']


  #For Symmetry
  elif target_name == "symmetry":
    if sim_score > magic_numbers['sym_similarity_threshold']:
      need_to_continue = True
    else:
      sim_score *= magic_numbers['sym_normalizing_factor_for_col_name']
    
  # For table
  elif target_name == "table":
    if sim_score >= magic_numbers['table_threshold_factor']:
      need_to_continue = True
    else:
      sim_score *= magic_numbers['table_normalizing_factor_for_col_name']

  elif target_name == "comments":
    if sim_score > magic_numbers['comments_similarity_threshold']:
      need_to_continue = True
    else:
      sim_score *= magic_numbers['comments_normalizing_factor_for_col_name']

  elif target_name == "price per carat":
    if sim_score > magic_numbers['ppc_similarity_threshold']:
      need_to_continue = True
    else:
      sim_score *= magic_numbers['ppc_normalizing_factor_for_col_name']

  elif target_name == "discount":
    if sim_score > magic_numbers['disc_similarity_threshold']:
      need_to_continue = True
    else:
      sim_score *= magic_numbers['disc_normalizing_factor_for_col_name']

  elif target_name == "total":
    if sim_score > magic_numbers['amt_similarity_threshold']:
      need_to_continue = True
    else:
      sim_score *= magic_numbers['amt_normalizing_factor_for_col_name']

  elif target_name == "rap price total":
    if sim_score > magic_numbers['raptotal_similarity_threshold']:
      need_to_continue = True
    else:
      sim_score *= magic_numbers['raptotal_normalizing_factor_for_col_name']

  else:
    raise Exception("The function could not find this target name")
  
  return sim_score, need_to_continue

def merge_similarity_score(sim_score_name,sim_score_val, target_name,magic_numbers):
  """
  This functionm will merge similarity score calculated from column name and column values

  Args:
  sim_score_name: Modified similarity score calculated from name
  sim_score_val: similarityb score calculated from value
  target_name: The name of target column
  magic_numbers(dict) = magic numbers in form of dictionary

  returns:
  final_similarity_score
  """

  # For Clarity
  if target_name == "clarity":
    final_similarity_score = sim_score_name + sim_score_val * magic_numbers['clarity_normalizing_factor_for_col_value']

  # For Carat
  elif target_name == "carat":
    final_similarity_score = sim_score_name + (sim_score_val*magic_numbers['carat_normalizing_factor_for_col_value'])
  
  # For Color
  elif target_name == "color":
    final_similarity_score = sim_score_name + sim_score_val * magic_numbers['color_normalizing_factor_for_col_value']
  
  # For shape (Modification Remaining and will be done in future)
  elif target_name == "shape":
      final_similarity_score = sim_score_name
  
  # Fluorescent
  elif target_name == "fluorescent":
    final_similarity_score = sim_score_name + sim_score_val * magic_numbers['fluor_normalizing_factor_for_col_value']
  
  # Raprate
  elif target_name == "raprate":
    final_similarity_score = sim_score_name + (sim_score_val*magic_numbers['raprate_normalizing_factor_for_col_value'])
  
  elif target_name in ["length","width","depth"]:
    final_similarity_score = sim_score_name + (sim_score_val*magic_numbers['measurement_normalizing_factor_for_col_value'])
  
  #Cut 
  elif target_name == "cut":
    final_similarity_score = sim_score_name + sim_score_val * magic_numbers['cut_normalizing_factor_for_col_value']
            
  #Polish      
  elif target_name == "polish":
    final_similarity_score = sim_score_name + sim_score_val * magic_numbers['polish_normalizing_factor_for_col_value']

  #symmetry          
  elif target_name == "symmetry":
    final_similarity_score = sim_score_name + sim_score_val * magic_numbers['sym_normalizing_factor_for_col_value']
    
  elif target_name == "table":
    final_similarity_score = sim_score_name + (sim_score_val*magic_numbers['table_normalizing_factor_for_col_value'])
    
  elif target_name == "comments":
    final_similarity_score = sim_score_name + sim_score_val * magic_numbers['comments_normalizing_factor_for_col_value']

  elif target_name == "price per carat":
    final_similarity_score = sim_score_name + sim_score_val * magic_numbers['ppc_normalizing_factor_for_col_value']

  elif target_name == "discount":
    final_similarity_score = sim_score_name + sim_score_val * magic_numbers['disc_normalizing_factor_for_col_value']
  
  elif target_name == "total":
    final_similarity_score = sim_score_name + sim_score_val * magic_numbers['amt_normalizing_factor_for_col_value']
  
  elif target_name == "rap price total":
    final_similarity_score = sim_score_name + sim_score_val * magic_numbers['raptotal_normalizing_factor_for_col_value']

  else:
    raise Exception("The function could not find this target name")
  
  return final_similarity_score