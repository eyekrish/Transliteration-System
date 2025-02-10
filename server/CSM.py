mapping = {
    chr(70670): {'char': 'k', 'type': 'consonant'},
    chr(70671): {'char': 'kh', 'type': 'consonant'},
    chr(70672): {'char': 'g', 'type': 'consonant'},
    chr(70673): {'char': 'gh', 'type': 'consonant'},
    chr(70674): {'char': 'ng', 'type': 'consonant'},
    chr(70675): {'char': 'ngh', 'type': 'consonant'},
    chr(70676): {'char': 'ch', 'type': 'consonant'},
    chr(70677): {'char': 'cha', 'type': 'consonant'},
    chr(70678): {'char': 'j', 'type': 'consonant'},
    chr(70679): {'char': 'jh', 'type': 'consonant'},
    chr(70680): {'char': 'ny', 'type': 'consonant'},
    chr(70681): {'char': 'nyh', 'type': 'consonant'},
    chr(70682): {'char': 'tt', 'type': 'consonant'},
    chr(70683): {'char': 'tth', 'type': 'consonant'},
    chr(70684): {'char': 'dd', 'type': 'consonant'},
    chr(70685): {'char': 'ddh', 'type': 'consonant'},
    chr(70686): {'char': 'nn', 'type': 'consonant'},
    chr(70687): {'char': 't', 'type': 'consonant'},
    chr(70688): {'char': 'th', 'type': 'consonant'},
    chr(70689): {'char': 'd', 'type': 'consonant'},
    chr(70690): {'char': 'dh', 'type': 'consonant'},
    chr(70691): {'char': 'n', 'type': 'consonant'},
    chr(70692): {'char': 'nh', 'type': 'consonant'},
    chr(70693): {'char': 'p', 'type': 'consonant'},
    chr(70694): {'char': 'ph', 'type': 'consonant'},
    chr(70695): {'char': 'b', 'type': 'consonant'},
    chr(70696): {'char': 'bh', 'type': 'consonant'},
    chr(70697): {'char': 'm', 'type': 'consonant'},
    chr(70698): {'char': 'mh', 'type': 'consonant'},
    chr(70699): {'char': 'y', 'type': 'consonant'},
    chr(70700): {'char': 'r', 'type': 'consonant'},
    chr(70701): {'char': 'rh', 'type': 'consonant'},
    chr(70702): {'char': 'l', 'type': 'consonant'},
    chr(70703): {'char': 'lh', 'type': 'consonant'},
    chr(70704): {'char': 'w', 'type': 'consonant'},
    chr(70705): {'char': 'sh', 'type': 'consonant'},
    chr(70706): {'char': 'ss', 'type': 'consonant'},
    chr(70707): {'char': 's', 'type': 'consonant'},
    chr(70708): {'char': 'h', 'type': 'consonant'},
    # independent Vowels
    chr(70656): {'char': 'a', 'type': 'vowel'},
    chr(70657): {'char': 'aa', 'type': 'vowel'},
    chr(70658): {'char': 'i', 'type': 'vowel'},
    chr(70659): {'char': 'ii', 'type': 'vowel'},
    chr(70660): {'char': 'u', 'type': 'vowel'},
    chr(70661): {'char': 'uu', 'type': 'vowel'},
    chr(70662): {'char': 'r', 'type': 'vowel'},
    chr(70663): {'char': 'rr', 'type': 'vowel'},
    chr(70664): {'char': 'l', 'type': 'vowel'},
    chr(70665): {'char': 'll', 'type': 'vowel'},
    chr(70666): {'char': 'e', 'type': 'vowel'},
    chr(70667): {'char': 'ai', 'type': 'vowel'},
    chr(70668): {'char': 'o', 'type': 'vowel'},
    chr(70669): {'char': 'au', 'type': 'vowel'},
    #dependent vowels

    chr(70709): {'char': 'a', 'type': 'dependent_vowel'},  
    chr(70710): {'char': 'i', 'type': 'dependent_vowel'},  
    chr(70711): {'char': 'ii', 'type': 'dependent_vowel'},  
    chr(70712): {'char': 'u', 'type': 'dependent_vowel'},  
    chr(70713): {'char': 'uu', 'type': 'dependent_vowel'}, 
    chr(70714): {'char': 'r', 'type': 'dependent_vowel'},  
    chr(70715): {'char': 'rr', 'type': 'dependent_vowel'},  
    chr(70716): {'char': 'l', 'type': 'dependent_vowel'},  
    chr(70717): {'char': 'll', 'type': 'dependent_vowel'},  
    chr(70718): {'char': 'e', 'type': 'dependent_vowel'},  
    chr(70719): {'char': 'ai', 'type': 'dependent_vowel'}, 
    chr(70720): {'char': 'o', 'type': 'dependent_vowel'},  
    chr(70721): {'char': 'au', 'type': 'dependent_vowel'}, 


    #consonant + dependent vowel

    chr(70670) + chr(70709): {'char': 'ka', 'type': 'consonant_dependent_vowel'},  # a
    chr(70670) + chr(70710): {'char': 'ki', 'type': 'consonant_dependent_vowel'},  # i
    chr(70670) + chr(70711): {'char': 'kii', 'type': 'consonant_dependent_vowel'}, # ii 
    chr(70670) + chr(70712): {'char': 'ku', 'type': 'consonant_dependent_vowel'},  # u
    chr(70670) + chr(70713): {'char': 'kuu', 'type': 'consonant_dependent_vowel'}, # uu 
    chr(70670) + chr(70714): {'char': 'kr', 'type': 'consonant_dependent_vowel'},  # r
    chr(70670) + chr(70715): {'char': 'krr', 'type': 'consonant_dependent_vowel'}, # rr
    chr(70670) + chr(70716): {'char': 'kl', 'type': 'consonant_dependent_vowel'},  # l
    chr(70670) + chr(70717): {'char': 'kll', 'type': 'consonant_dependent_vowel'}, # ll 
    chr(70670) + chr(70718): {'char': 'ke', 'type': 'consonant_dependent_vowel'},  # e
    chr(70670) + chr(70719): {'char': 'kai', 'type': 'consonant_dependent_vowel'}, # ai
    chr(70670) + chr(70720): {'char': 'ko', 'type': 'consonant_dependent_vowel'},  # o
    chr(70670) + chr(70721): {'char': 'kau', 'type': 'consonant_dependent_vowel'}, # au


    chr(70671) + chr(70709): {'char': 'kha', 'type': 'consonant_dependent_vowel'},  # a
    chr(70671) + chr(70710): {'char': 'khi', 'type': 'consonant_dependent_vowel'},  # i
    chr(70671) + chr(70711): {'char': 'khii', 'type': 'consonant_dependent_vowel'}, # ii (if allowed)
    chr(70671) + chr(70712): {'char': 'khu', 'type': 'consonant_dependent_vowel'},  # u
    chr(70671) + chr(70713): {'char': 'khuu', 'type': 'consonant_dependent_vowel'}, # uu (if allowed)
    chr(70671) + chr(70714): {'char': 'khr', 'type': 'consonant_dependent_vowel'},  # r
    chr(70671) + chr(70715): {'char': 'khrr', 'type': 'consonant_dependent_vowel'}, # rr (if allowed)
    chr(70671) + chr(70716): {'char': 'khl', 'type': 'consonant_dependent_vowel'},  # l
    chr(70671) + chr(70717): {'char': 'khll', 'type': 'consonant_dependent_vowel'}, # ll (if allowed)
    chr(70671) + chr(70718): {'char': 'khe', 'type': 'consonant_dependent_vowel'},  # e
    chr(70671) + chr(70719): {'char': 'khai', 'type': 'consonant_dependent_vowel'}, # ai
    chr(70671) + chr(70720): {'char': 'kho', 'type': 'consonant_dependent_vowel'},  # o
    chr(70671) + chr(70721): {'char': 'khau', 'type': 'consonant_dependent_vowel'}, # au


    
    chr(70672) + chr(70709): {'char': 'ga', 'type': 'consonant_dependent_vowel'},  # a
    chr(70672) + chr(70710): {'char': 'gi', 'type': 'consonant_dependent_vowel'},  # i
    chr(70672) + chr(70711): {'char': 'gii', 'type': 'consonant_dependent_vowel'}, # ii (if allowed)
    chr(70672) + chr(70712): {'char': 'gu', 'type': 'consonant_dependent_vowel'},  # u
    chr(70672) + chr(70713): {'char': 'guu', 'type': 'consonant_dependent_vowel'}, # uu (if allowed)
    chr(70672) + chr(70714): {'char': 'gr', 'type': 'consonant_dependent_vowel'},  # r
    chr(70672) + chr(70715): {'char': 'grr', 'type': 'consonant_dependent_vowel'}, # rr (if allowed)
    chr(70672) + chr(70716): {'char': 'gl', 'type': 'consonant_dependent_vowel'},  # l
    chr(70672) + chr(70717): {'char': 'gll', 'type': 'consonant_dependent_vowel'}, # ll (if allowed)
    chr(70672) + chr(70718): {'char': 'ge', 'type': 'consonant_dependent_vowel'},  # e
    chr(70672) + chr(70719): {'char': 'gai', 'type': 'consonant_dependent_vowel'}, # ai
    chr(70672) + chr(70720): {'char': 'go', 'type': 'consonant_dependent_vowel'},  # o
    chr(70672) + chr(70721): {'char': 'gau', 'type': 'consonant_dependent_vowel'}, # au



    chr(70673) + chr(70709): {'char': 'gha', 'type': 'consonant_dependent_vowel'},
    chr(70673) + chr(70710): {'char': 'ghi', 'type': 'consonant_dependent_vowel'},
    chr(70673) + chr(70711): {'char': 'ghii', 'type': 'consonant_dependent_vowel'},
    chr(70673) + chr(70712): {'char': 'ghu', 'type': 'consonant_dependent_vowel'},
    chr(70673) + chr(70713): {'char': 'ghuu', 'type': 'consonant_dependent_vowel'},
    chr(70673) + chr(70714): {'char': 'ghr', 'type': 'consonant_dependent_vowel'},
    chr(70673) + chr(70715): {'char': 'ghrr', 'type': 'consonant_dependent_vowel'},
    chr(70673) + chr(70716): {'char': 'ghl', 'type': 'consonant_dependent_vowel'},
    chr(70673) + chr(70717): {'char': 'ghll', 'type': 'consonant_dependent_vowel'},
    chr(70673) + chr(70718): {'char': 'ghe', 'type': 'consonant_dependent_vowel'},
    chr(70673) + chr(70719): {'char': 'ghai', 'type': 'consonant_dependent_vowel'},
    chr(70673) + chr(70720): {'char': 'gho', 'type': 'consonant_dependent_vowel'},
    chr(70673) + chr(70721): {'char': 'ghau', 'type': 'consonant_dependent_vowel'},



    chr(70674) + chr(70709): {'char': 'nga', 'type': 'consonant_dependent_vowel'},
    chr(70674) + chr(70710): {'char': 'ngi', 'type': 'consonant_dependent_vowel'},
    chr(70674) + chr(70711): {'char': 'ngii', 'type': 'consonant_dependent_vowel'},
    chr(70674) + chr(70712): {'char': 'ngu', 'type': 'consonant_dependent_vowel'},
    chr(70674) + chr(70713): {'char': 'nguu', 'type': 'consonant_dependent_vowel'},
    chr(70674) + chr(70714): {'char': 'ngr', 'type': 'consonant_dependent_vowel'},
    chr(70674) + chr(70715): {'char': 'ngrr', 'type': 'consonant_dependent_vowel'},
    chr(70674) + chr(70716): {'char': 'ngl', 'type': 'consonant_dependent_vowel'},
    chr(70674) + chr(70717): {'char': 'ngll', 'type': 'consonant_dependent_vowel'},
    chr(70674) + chr(70718): {'char': 'nge', 'type': 'consonant_dependent_vowel'},
    chr(70674) + chr(70719): {'char': 'ngai', 'type': 'consonant_dependent_vowel'},
    chr(70674) + chr(70720): {'char': 'ngo', 'type': 'consonant_dependent_vowel'},
    chr(70674) + chr(70721): {'char': 'ngau', 'type': 'consonant_dependent_vowel'},



    chr(70675) + chr(70709): {'char': 'ngha', 'type': 'consonant_dependent_vowel'},
    chr(70675) + chr(70710): {'char': 'nghi', 'type': 'consonant_dependent_vowel'},
    chr(70675) + chr(70711): {'char': 'nghii', 'type': 'consonant_dependent_vowel'},
    chr(70675) + chr(70712): {'char': 'nghu', 'type': 'consonant_dependent_vowel'},
    chr(70675) + chr(70713): {'char': 'nghuu', 'type': 'consonant_dependent_vowel'},
    chr(70675) + chr(70714): {'char': 'nghr', 'type': 'consonant_dependent_vowel'},
    chr(70675) + chr(70715): {'char': 'nghrr', 'type': 'consonant_dependent_vowel'},
    chr(70675) + chr(70716): {'char': 'nghl', 'type': 'consonant_dependent_vowel'},
    chr(70675) + chr(70717): {'char': 'nghll', 'type': 'consonant_dependent_vowel'},
    chr(70675) + chr(70718): {'char': 'nghe', 'type': 'consonant_dependent_vowel'},
    chr(70675) + chr(70719): {'char': 'nghai', 'type': 'consonant_dependent_vowel'},
    chr(70675) + chr(70720): {'char': 'ngho', 'type': 'consonant_dependent_vowel'},
    chr(70675) + chr(70721): {'char': 'nghau', 'type': 'consonant_dependent_vowel'},



    chr(70676) + chr(70709): {'char': 'cha', 'type': 'consonant_dependent_vowel'},
    chr(70676) + chr(70710): {'char': 'chi', 'type': 'consonant_dependent_vowel'},
    chr(70676) + chr(70711): {'char': 'chii', 'type': 'consonant_dependent_vowel'},
    chr(70676) + chr(70712): {'char': 'chu', 'type': 'consonant_dependent_vowel'},
    chr(70676) + chr(70713): {'char': 'chuu', 'type': 'consonant_dependent_vowel'},
    chr(70676) + chr(70714): {'char': 'chr', 'type': 'consonant_dependent_vowel'},
    chr(70676) + chr(70715): {'char': 'chrr', 'type': 'consonant_dependent_vowel'},
    chr(70676) + chr(70716): {'char': 'chl', 'type': 'consonant_dependent_vowel'},
    chr(70676) + chr(70717): {'char': 'chll', 'type': 'consonant_dependent_vowel'},
    chr(70676) + chr(70718): {'char': 'che', 'type': 'consonant_dependent_vowel'},
    chr(70676) + chr(70719): {'char': 'chai', 'type': 'consonant_dependent_vowel'},
    chr(70676) + chr(70720): {'char': 'cho', 'type': 'consonant_dependent_vowel'},
    chr(70676) + chr(70721): {'char': 'chau', 'type': 'consonant_dependent_vowel'},



    chr(70677) + chr(70709): {'char': 'cha', 'type': 'consonant_dependent_vowel'},  # a
    chr(70677) + chr(70710): {'char': 'chi', 'type': 'consonant_dependent_vowel'},  # i
    chr(70677) + chr(70711): {'char': 'chii', 'type': 'consonant_dependent_vowel'}, # ii (if allowed)
    chr(70677) + chr(70712): {'char': 'chu', 'type': 'consonant_dependent_vowel'},  # u
    chr(70677) + chr(70713): {'char': 'chuu', 'type': 'consonant_dependent_vowel'}, # uu (if allowed)
    chr(70677) + chr(70714): {'char': 'chr', 'type': 'consonant_dependent_vowel'},  # r
    chr(70677) + chr(70715): {'char': 'chrr', 'type': 'consonant_dependent_vowel'}, # rr (if allowed)
    chr(70677) + chr(70716): {'char': 'chl', 'type': 'consonant_dependent_vowel'},  # l
    chr(70677) + chr(70717): {'char': 'chll', 'type': 'consonant_dependent_vowel'}, # ll (if allowed)
    chr(70677) + chr(70718): {'char': 'che', 'type': 'consonant_dependent_vowel'},  # e
    chr(70677) + chr(70719): {'char': 'chai', 'type': 'consonant_dependent_vowel'}, # ai
    chr(70677) + chr(70720): {'char': 'cho', 'type': 'consonant_dependent_vowel'},  # o
    chr(70677) + chr(70721): {'char': 'chau', 'type': 'consonant_dependent_vowel'}, # au


    chr(70678) + chr(70709): {'char': 'ja', 'type': 'consonant_dependent_vowel'},  # a
    chr(70678) + chr(70710): {'char': 'ji', 'type': 'consonant_dependent_vowel'},  # i
    chr(70678) + chr(70711): {'char': 'jii', 'type': 'consonant_dependent_vowel'}, # ii (if allowed)
    chr(70678) + chr(70712): {'char': 'ju', 'type': 'consonant_dependent_vowel'},  # u
    chr(70678) + chr(70713): {'char': 'juu', 'type': 'consonant_dependent_vowel'}, # uu (if allowed)
    chr(70678) + chr(70714): {'char': 'jr', 'type': 'consonant_dependent_vowel'},  # r
    chr(70678) + chr(70715): {'char': 'jrr', 'type': 'consonant_dependent_vowel'}, # rr (if allowed)
    chr(70678) + chr(70716): {'char': 'jl', 'type': 'consonant_dependent_vowel'},  # l
    chr(70678) + chr(70717): {'char': 'jll', 'type': 'consonant_dependent_vowel'}, # ll (if allowed)
    chr(70678) + chr(70718): {'char': 'je', 'type': 'consonant_dependent_vowel'},  # e
    chr(70678) + chr(70719): {'char': 'jai', 'type': 'consonant_dependent_vowel'}, # ai
    chr(70678) + chr(70720): {'char': 'jo', 'type': 'consonant_dependent_vowel'},  # o
    chr(70678) + chr(70721): {'char': 'jau', 'type': 'consonant_dependent_vowel'}, # au


    # For `chr(70679)` (jh)
    chr(70679) + chr(70709): {'char': 'jha', 'type': 'consonant_dependent_vowel'},
    chr(70679) + chr(70710): {'char': 'jhi', 'type': 'consonant_dependent_vowel'},
    chr(70679) + chr(70711): {'char': 'jhii', 'type': 'consonant_dependent_vowel'},
    chr(70679) + chr(70712): {'char': 'jhu', 'type': 'consonant_dependent_vowel'},
    chr(70679) + chr(70713): {'char': 'jhuu', 'type': 'consonant_dependent_vowel'},
    chr(70679) + chr(70714): {'char': 'jhr', 'type': 'consonant_dependent_vowel'},
    chr(70679) + chr(70715): {'char': 'jhrr', 'type': 'consonant_dependent_vowel'},
    chr(70679) + chr(70716): {'char': 'jhl', 'type': 'consonant_dependent_vowel'},
    chr(70679) + chr(70717): {'char': 'jhll', 'type': 'consonant_dependent_vowel'},
    chr(70679) + chr(70718): {'char': 'jhe', 'type': 'consonant_dependent_vowel'},
    chr(70679) + chr(70719): {'char': 'jhai', 'type': 'consonant_dependent_vowel'},
    chr(70679) + chr(70720): {'char': 'jho', 'type': 'consonant_dependent_vowel'},
    chr(70679) + chr(70721): {'char': 'jhau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70680)` (ny)
    chr(70680) + chr(70709): {'char': 'nya', 'type': 'consonant_dependent_vowel'},
    chr(70680) + chr(70710): {'char': 'nyi', 'type': 'consonant_dependent_vowel'},
    chr(70680) + chr(70711): {'char': 'nyii', 'type': 'consonant_dependent_vowel'},
    chr(70680) + chr(70712): {'char': 'nyu', 'type': 'consonant_dependent_vowel'},
    chr(70680) + chr(70713): {'char': 'nyuu', 'type': 'consonant_dependent_vowel'},
    chr(70680) + chr(70714): {'char': 'nyr', 'type': 'consonant_dependent_vowel'},
    chr(70680) + chr(70715): {'char': 'nyrr', 'type': 'consonant_dependent_vowel'},
    chr(70680) + chr(70716): {'char': 'nyl', 'type': 'consonant_dependent_vowel'},
    chr(70680) + chr(70717): {'char': 'nyll', 'type': 'consonant_dependent_vowel'},
    chr(70680) + chr(70718): {'char': 'nye', 'type': 'consonant_dependent_vowel'},
    chr(70680) + chr(70719): {'char': 'nyai', 'type': 'consonant_dependent_vowel'},
    chr(70680) + chr(70720): {'char': 'nyo', 'type': 'consonant_dependent_vowel'},
    chr(70680) + chr(70721): {'char': 'nyau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70681)` (ny)
    chr(70681) + chr(70709): {'char': 'nya', 'type': 'consonant_dependent_vowel'},
    chr(70681) + chr(70710): {'char': 'nyi', 'type': 'consonant_dependent_vowel'},
    chr(70681) + chr(70711): {'char': 'nyii', 'type': 'consonant_dependent_vowel'},
    chr(70681) + chr(70712): {'char': 'nyu', 'type': 'consonant_dependent_vowel'},
    chr(70681) + chr(70713): {'char': 'nyuu', 'type': 'consonant_dependent_vowel'},
    chr(70681) + chr(70714): {'char': 'nyr', 'type': 'consonant_dependent_vowel'},
    chr(70681) + chr(70715): {'char': 'nyrr', 'type': 'consonant_dependent_vowel'},
    chr(70681) + chr(70716): {'char': 'nyl', 'type': 'consonant_dependent_vowel'},
    chr(70681) + chr(70717): {'char': 'nyll', 'type': 'consonant_dependent_vowel'},
    chr(70681) + chr(70718): {'char': 'nye', 'type': 'consonant_dependent_vowel'},
    chr(70681) + chr(70719): {'char': 'nyai', 'type': 'consonant_dependent_vowel'},
    chr(70681) + chr(70720): {'char': 'nyo', 'type': 'consonant_dependent_vowel'},
    chr(70681) + chr(70721): {'char': 'nyau', 'type': 'consonant_dependent_vowel'},



    # For `chr(70682)` (tt)
    chr(70682) + chr(70709): {'char': 'tta', 'type': 'consonant_dependent_vowel'},
    chr(70682) + chr(70710): {'char': 'tti', 'type': 'consonant_dependent_vowel'},
    chr(70682) + chr(70711): {'char': 'ttii', 'type': 'consonant_dependent_vowel'},
    chr(70682) + chr(70712): {'char': 'ttu', 'type': 'consonant_dependent_vowel'},
    chr(70682) + chr(70713): {'char': 'ttuu', 'type': 'consonant_dependent_vowel'},
    chr(70682) + chr(70714): {'char': 'ttr', 'type': 'consonant_dependent_vowel'},
    chr(70682) + chr(70715): {'char': 'ttrr', 'type': 'consonant_dependent_vowel'},
    chr(70682) + chr(70716): {'char': 'ttl', 'type': 'consonant_dependent_vowel'},
    chr(70682) + chr(70717): {'char': 'ttll', 'type': 'consonant_dependent_vowel'},
    chr(70682) + chr(70718): {'char': 'tte', 'type': 'consonant_dependent_vowel'},
    chr(70682) + chr(70719): {'char': 'ttai', 'type': 'consonant_dependent_vowel'},
    chr(70682) + chr(70720): {'char': 'tto', 'type': 'consonant_dependent_vowel'},
    chr(70682) + chr(70721): {'char': 'ttau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70683)` (tth)
    chr(70683) + chr(70709): {'char': 'ttha', 'type': 'consonant_dependent_vowel'},
    chr(70683) + chr(70710): {'char': 'tthi', 'type': 'consonant_dependent_vowel'},
    chr(70683) + chr(70711): {'char': 'tthii', 'type': 'consonant_dependent_vowel'},
    chr(70683) + chr(70712): {'char': 'tthu', 'type': 'consonant_dependent_vowel'},
    chr(70683) + chr(70713): {'char': 'tthuu', 'type': 'consonant_dependent_vowel'},
    chr(70683) + chr(70714): {'char': 'tthr', 'type': 'consonant_dependent_vowel'},
    chr(70683) + chr(70715): {'char': 'tthrr', 'type': 'consonant_dependent_vowel'},
    chr(70683) + chr(70716): {'char': 'tthl', 'type': 'consonant_dependent_vowel'},
    chr(70683) + chr(70717): {'char': 'tthll', 'type': 'consonant_dependent_vowel'},
    chr(70683) + chr(70718): {'char': 'tthe', 'type': 'consonant_dependent_vowel'},
    chr(70683) + chr(70719): {'char': 'tthai', 'type': 'consonant_dependent_vowel'},
    chr(70683) + chr(70720): {'char': 'ttho', 'type': 'consonant_dependent_vowel'},
    chr(70683) + chr(70721): {'char': 'ttau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70684)` (dd)
    chr(70684) + chr(70709): {'char': 'dda', 'type': 'consonant_dependent_vowel'},
    chr(70684) + chr(70710): {'char': 'ddi', 'type': 'consonant_dependent_vowel'},
    chr(70684) + chr(70711): {'char': 'ddii', 'type': 'consonant_dependent_vowel'},
    chr(70684) + chr(70712): {'char': 'ddu', 'type': 'consonant_dependent_vowel'},
    chr(70684) + chr(70713): {'char': 'dduu', 'type': 'consonant_dependent_vowel'},
    chr(70684) + chr(70714): {'char': 'ddr', 'type': 'consonant_dependent_vowel'},
    chr(70684) + chr(70715): {'char': 'ddrr', 'type': 'consonant_dependent_vowel'},
    chr(70684) + chr(70716): {'char': 'ddl', 'type': 'consonant_dependent_vowel'},
    chr(70684) + chr(70717): {'char': 'ddll', 'type': 'consonant_dependent_vowel'},
    chr(70684) + chr(70718): {'char': 'dde', 'type': 'consonant_dependent_vowel'},
    chr(70684) + chr(70719): {'char': 'ddai', 'type': 'consonant_dependent_vowel'},
    chr(70684) + chr(70720): {'char': 'ddo', 'type': 'consonant_dependent_vowel'},
    chr(70684) + chr(70721): {'char': 'ddau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70685)` (ddh)
    chr(70685) + chr(70709): {'char': 'ddha', 'type': 'consonant_dependent_vowel'},
    chr(70685) + chr(70710): {'char': 'ddhi', 'type': 'consonant_dependent_vowel'},
    chr(70685) + chr(70711): {'char': 'ddhii', 'type': 'consonant_dependent_vowel'},
    chr(70685) + chr(70712): {'char': 'ddhu', 'type': 'consonant_dependent_vowel'},
    chr(70685) + chr(70713): {'char': 'ddhuu', 'type': 'consonant_dependent_vowel'},
    chr(70685) + chr(70714): {'char': 'ddhr', 'type': 'consonant_dependent_vowel'},
    chr(70685) + chr(70715): {'char': 'ddhrr', 'type': 'consonant_dependent_vowel'},
    chr(70685) + chr(70716): {'char': 'ddhl', 'type': 'consonant_dependent_vowel'},
    chr(70685) + chr(70717): {'char': 'ddhll', 'type': 'consonant_dependent_vowel'},
    chr(70685) + chr(70718): {'char': 'ddhe', 'type': 'consonant_dependent_vowel'},
    chr(70685) + chr(70719): {'char': 'ddhai', 'type': 'consonant_dependent_vowel'},
    chr(70685) + chr(70720): {'char': 'ddho', 'type': 'consonant_dependent_vowel'},
    chr(70685) + chr(70721): {'char': 'ddhau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70686)` (nn)
    chr(70686) + chr(70709): {'char': 'nna', 'type': 'consonant_dependent_vowel'},
    chr(70686) + chr(70710): {'char': 'nni', 'type': 'consonant_dependent_vowel'},
    chr(70686) + chr(70711): {'char': 'nnii', 'type': 'consonant_dependent_vowel'},
    chr(70686) + chr(70712): {'char': 'nnu', 'type': 'consonant_dependent_vowel'},
    chr(70686) + chr(70713): {'char': 'nnuu', 'type': 'consonant_dependent_vowel'},
    chr(70686) + chr(70714): {'char': 'nnr', 'type': 'consonant_dependent_vowel'},
    chr(70686) + chr(70715): {'char': 'nnrr', 'type': 'consonant_dependent_vowel'},
    chr(70686) + chr(70716): {'char': 'nnl', 'type': 'consonant_dependent_vowel'},
    chr(70686) + chr(70717): {'char': 'nnll', 'type': 'consonant_dependent_vowel'},
    chr(70686) + chr(70718): {'char': 'nne', 'type': 'consonant_dependent_vowel'},
    chr(70686) + chr(70719): {'char': 'nnai', 'type': 'consonant_dependent_vowel'},
    chr(70686) + chr(70720): {'char': 'nno', 'type': 'consonant_dependent_vowel'},
    chr(70686) + chr(70721): {'char': 'nnau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70687)` (t)
    chr(70687) + chr(70709): {'char': 'ta', 'type': 'consonant_dependent_vowel'},
    chr(70687) + chr(70710): {'char': 'ti', 'type': 'consonant_dependent_vowel'},
    chr(70687) + chr(70711): {'char': 'tii', 'type': 'consonant_dependent_vowel'},
    chr(70687) + chr(70712): {'char': 'tu', 'type': 'consonant_dependent_vowel'},
    chr(70687) + chr(70713): {'char': 'tuu', 'type': 'consonant_dependent_vowel'},
    chr(70687) + chr(70714): {'char': 'tr', 'type': 'consonant_dependent_vowel'},
    chr(70687) + chr(70715): {'char': 'trr', 'type': 'consonant_dependent_vowel'},
    chr(70687) + chr(70716): {'char': 'tl', 'type': 'consonant_dependent_vowel'},
    chr(70687) + chr(70717): {'char': 'tll', 'type': 'consonant_dependent_vowel'},
    chr(70687) + chr(70718): {'char': 'te', 'type': 'consonant_dependent_vowel'},
    chr(70687) + chr(70719): {'char': 'tai', 'type': 'consonant_dependent_vowel'},
    chr(70687) + chr(70720): {'char': 'to', 'type': 'consonant_dependent_vowel'},
    chr(70687) + chr(70721): {'char': 'tau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70688)` (th)
    chr(70688) + chr(70709): {'char': 'tha', 'type': 'consonant_dependent_vowel'},
    chr(70688) + chr(70710): {'char': 'thi', 'type': 'consonant_dependent_vowel'},
    chr(70688) + chr(70711): {'char': 'thii', 'type': 'consonant_dependent_vowel'},
    chr(70688) + chr(70712): {'char': 'thu', 'type': 'consonant_dependent_vowel'},
    chr(70688) + chr(70713): {'char': 'thuu', 'type': 'consonant_dependent_vowel'},
    chr(70688) + chr(70714): {'char': 'thr', 'type': 'consonant_dependent_vowel'},
    chr(70688) + chr(70715): {'char': 'thrr', 'type': 'consonant_dependent_vowel'},
    chr(70688) + chr(70716): {'char': 'thl', 'type': 'consonant_dependent_vowel'},
    chr(70688) + chr(70717): {'char': 'thll', 'type': 'consonant_dependent_vowel'},
    chr(70688) + chr(70718): {'char': 'the', 'type': 'consonant_dependent_vowel'},
    chr(70688) + chr(70719): {'char': 'thai', 'type': 'consonant_dependent_vowel'},
    chr(70688) + chr(70720): {'char': 'tho', 'type': 'consonant_dependent_vowel'},
    chr(70688) + chr(70721): {'char': 'thau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70689)` (d)
    chr(70689) + chr(70709): {'char': 'da', 'type': 'consonant_dependent_vowel'},
    chr(70689) + chr(70710): {'char': 'di', 'type': 'consonant_dependent_vowel'},
    chr(70689) + chr(70711): {'char': 'dii', 'type': 'consonant_dependent_vowel'},
    chr(70689) + chr(70712): {'char': 'du', 'type': 'consonant_dependent_vowel'},
    chr(70689) + chr(70713): {'char': 'duu', 'type': 'consonant_dependent_vowel'},
    chr(70689) + chr(70714): {'char': 'dr', 'type': 'consonant_dependent_vowel'},
    chr(70689) + chr(70715): {'char': 'drr', 'type': 'consonant_dependent_vowel'},
    chr(70689) + chr(70716): {'char': 'dl', 'type': 'consonant_dependent_vowel'},
    chr(70689) + chr(70717): {'char': 'dll', 'type': 'consonant_dependent_vowel'},
    chr(70689) + chr(70718): {'char': 'de', 'type': 'consonant_dependent_vowel'},
    chr(70689) + chr(70719): {'char': 'dai', 'type': 'consonant_dependent_vowel'},
    chr(70689) + chr(70720): {'char': 'do', 'type': 'consonant_dependent_vowel'},
    chr(70689) + chr(70721): {'char': 'dau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70690)` (dh)
    chr(70690) + chr(70709): {'char': 'dha', 'type': 'consonant_dependent_vowel'},
    chr(70690) + chr(70710): {'char': 'dhi', 'type': 'consonant_dependent_vowel'},
    chr(70690) + chr(70711): {'char': 'dhii', 'type': 'consonant_dependent_vowel'},
    chr(70690) + chr(70712): {'char': 'dhu', 'type': 'consonant_dependent_vowel'},
    chr(70690) + chr(70713): {'char': 'dhuu', 'type': 'consonant_dependent_vowel'},
    chr(70690) + chr(70714): {'char': 'dhr', 'type': 'consonant_dependent_vowel'},
    chr(70690) + chr(70715): {'char': 'dhrr', 'type': 'consonant_dependent_vowel'},
    chr(70690) + chr(70716): {'char': 'dhl', 'type': 'consonant_dependent_vowel'},
    chr(70690) + chr(70717): {'char': 'dhll', 'type': 'consonant_dependent_vowel'},
    chr(70690) + chr(70718): {'char': 'dhe', 'type': 'consonant_dependent_vowel'},
    chr(70690) + chr(70719): {'char': 'dhai', 'type': 'consonant_dependent_vowel'},
    chr(70690) + chr(70720): {'char': 'dho', 'type': 'consonant_dependent_vowel'},
    chr(70690) + chr(70721): {'char': 'dhau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70691)` (n)
    chr(70691) + chr(70709): {'char': 'na', 'type': 'consonant_dependent_vowel'},
    chr(70691) + chr(70710): {'char': 'ni', 'type': 'consonant_dependent_vowel'},
    chr(70691) + chr(70711): {'char': 'nii', 'type': 'consonant_dependent_vowel'},
    chr(70691) + chr(70712): {'char': 'nu', 'type': 'consonant_dependent_vowel'},
    chr(70691) + chr(70713): {'char': 'nuu', 'type': 'consonant_dependent_vowel'},
    chr(70691) + chr(70714): {'char': 'nr', 'type': 'consonant_dependent_vowel'},
    chr(70691) + chr(70715): {'char': 'nrr', 'type': 'consonant_dependent_vowel'},
    chr(70691) + chr(70716): {'char': 'nl', 'type': 'consonant_dependent_vowel'},
    chr(70691) + chr(70717): {'char': 'nll', 'type': 'consonant_dependent_vowel'},
    chr(70691) + chr(70718): {'char': 'ne', 'type': 'consonant_dependent_vowel'},
    chr(70691) + chr(70719): {'char': 'nai', 'type': 'consonant_dependent_vowel'},
    chr(70691) + chr(70720): {'char': 'no', 'type': 'consonant_dependent_vowel'},
    chr(70691) + chr(70721): {'char': 'nau', 'type': 'consonant_dependent_vowel'},
   
    # For `chr(70692)` (nh)
    chr(70692) + chr(70709): {'char': 'nha', 'type': 'consonant_dependent_vowel'},
    chr(70692) + chr(70710): {'char': 'nhi', 'type': 'consonant_dependent_vowel'},
    chr(70692) + chr(70711): {'char': 'nhii', 'type': 'consonant_dependent_vowel'},
    chr(70692) + chr(70712): {'char': 'nhu', 'type': 'consonant_dependent_vowel'},
    chr(70692) + chr(70713): {'char': 'nhuu', 'type': 'consonant_dependent_vowel'},
    chr(70692) + chr(70714): {'char': 'nhr', 'type': 'consonant_dependent_vowel'},
    chr(70692) + chr(70715): {'char': 'nhrr', 'type': 'consonant_dependent_vowel'},
    chr(70692) + chr(70716): {'char': 'nhl', 'type': 'consonant_dependent_vowel'},
    chr(70692) + chr(70717): {'char': 'nhll', 'type': 'consonant_dependent_vowel'},
    chr(70692) + chr(70718): {'char': 'nhe', 'type': 'consonant_dependent_vowel'},
    chr(70692) + chr(70719): {'char': 'nhai', 'type': 'consonant_dependent_vowel'},
    chr(70692) + chr(70720): {'char': 'nho', 'type': 'consonant_dependent_vowel'},
    chr(70692) + chr(70721): {'char': 'nhau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70693)` (p)
    chr(70693) + chr(70709): {'char': 'pa', 'type': 'consonant_dependent_vowel'},
    chr(70693) + chr(70710): {'char': 'pi', 'type': 'consonant_dependent_vowel'},
    chr(70693) + chr(70711): {'char': 'pii', 'type': 'consonant_dependent_vowel'},
    chr(70693) + chr(70712): {'char': 'pu', 'type': 'consonant_dependent_vowel'},
    chr(70693) + chr(70713): {'char': 'puu', 'type': 'consonant_dependent_vowel'},
    chr(70693) + chr(70714): {'char': 'pr', 'type': 'consonant_dependent_vowel'},
    chr(70693) + chr(70715): {'char': 'prr', 'type': 'consonant_dependent_vowel'},
    chr(70693) + chr(70716): {'char': 'pl', 'type': 'consonant_dependent_vowel'},
    chr(70693) + chr(70717): {'char': 'pll', 'type': 'consonant_dependent_vowel'},
    chr(70693) + chr(70718): {'char': 'pe', 'type': 'consonant_dependent_vowel'},
    chr(70693) + chr(70719): {'char': 'pai', 'type': 'consonant_dependent_vowel'},
    chr(70693) + chr(70720): {'char': 'po', 'type': 'consonant_dependent_vowel'},
    chr(70693) + chr(70721): {'char': 'pau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70694)` (ph)
    chr(70694) + chr(70709): {'char': 'pha', 'type': 'consonant_dependent_vowel'},
    chr(70694) + chr(70710): {'char': 'phi', 'type': 'consonant_dependent_vowel'},
    chr(70694) + chr(70711): {'char': 'phii', 'type': 'consonant_dependent_vowel'},
    chr(70694) + chr(70712): {'char': 'phu', 'type': 'consonant_dependent_vowel'},
    chr(70694) + chr(70713): {'char': 'phuu', 'type': 'consonant_dependent_vowel'},
    chr(70694) + chr(70714): {'char': 'phr', 'type': 'consonant_dependent_vowel'},
    chr(70694) + chr(70715): {'char': 'phrr', 'type': 'consonant_dependent_vowel'},
    chr(70694) + chr(70716): {'char': 'phl', 'type': 'consonant_dependent_vowel'},
    chr(70694) + chr(70717): {'char': 'phll', 'type': 'consonant_dependent_vowel'},
    chr(70694) + chr(70718): {'char': 'phe', 'type': 'consonant_dependent_vowel'},
    chr(70694) + chr(70719): {'char': 'phai', 'type': 'consonant_dependent_vowel'},
    chr(70694) + chr(70720): {'char': 'pho', 'type': 'consonant_dependent_vowel'},
    chr(70694) + chr(70721): {'char': 'phau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70695)` (b)
    chr(70695) + chr(70709): {'char': 'ba', 'type': 'consonant_dependent_vowel'},
    chr(70695) + chr(70710): {'char': 'bi', 'type': 'consonant_dependent_vowel'},
    chr(70695) + chr(70711): {'char': 'bii', 'type': 'consonant_dependent_vowel'},
    chr(70695) + chr(70712): {'char': 'bu', 'type': 'consonant_dependent_vowel'},
    chr(70695) + chr(70713): {'char': 'buu', 'type': 'consonant_dependent_vowel'},
    chr(70695) + chr(70714): {'char': 'br', 'type': 'consonant_dependent_vowel'},
    chr(70695) + chr(70715): {'char': 'brr', 'type': 'consonant_dependent_vowel'},
    chr(70695) + chr(70716): {'char': 'bl', 'type': 'consonant_dependent_vowel'},
    chr(70695) + chr(70717): {'char': 'bll', 'type': 'consonant_dependent_vowel'},
    chr(70695) + chr(70718): {'char': 'be', 'type': 'consonant_dependent_vowel'},
    chr(70695) + chr(70719): {'char': 'bai', 'type': 'consonant_dependent_vowel'},
    chr(70695) + chr(70720): {'char': 'bo', 'type': 'consonant_dependent_vowel'},
    chr(70695) + chr(70721): {'char': 'bau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70696)` (bh)
    chr(70696) + chr(70709): {'char': 'bha', 'type': 'consonant_dependent_vowel'},
    chr(70696) + chr(70710): {'char': 'bhi', 'type': 'consonant_dependent_vowel'},
    chr(70696) + chr(70711): {'char': 'bhii', 'type': 'consonant_dependent_vowel'},
    chr(70696) + chr(70712): {'char': 'bhu', 'type': 'consonant_dependent_vowel'},
    chr(70696) + chr(70713): {'char': 'bhuu', 'type': 'consonant_dependent_vowel'},
    chr(70696) + chr(70714): {'char': 'bhr', 'type': 'consonant_dependent_vowel'},
    chr(70696) + chr(70715): {'char': 'bhrr', 'type': 'consonant_dependent_vowel'},
    chr(70696) + chr(70716): {'char': 'bhl', 'type': 'consonant_dependent_vowel'},
    chr(70696) + chr(70717): {'char': 'bhll', 'type': 'consonant_dependent_vowel'},
    chr(70696) + chr(70718): {'char': 'bhe', 'type': 'consonant_dependent_vowel'},
    chr(70696) + chr(70719): {'char': 'bhai', 'type': 'consonant_dependent_vowel'},
    chr(70696) + chr(70720): {'char': 'bho', 'type': 'consonant_dependent_vowel'},
    chr(70696) + chr(70721): {'char': 'bhau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70697)` (m)
    chr(70697) + chr(70709): {'char': 'ma', 'type': 'consonant_dependent_vowel'},
    chr(70697) + chr(70710): {'char': 'mi', 'type': 'consonant_dependent_vowel'},
    chr(70697) + chr(70711): {'char': 'mii', 'type': 'consonant_dependent_vowel'},
    chr(70697) + chr(70712): {'char': 'mu', 'type': 'consonant_dependent_vowel'},
    chr(70697) + chr(70713): {'char': 'muu', 'type': 'consonant_dependent_vowel'},
    chr(70697) + chr(70714): {'char': 'mr', 'type': 'consonant_dependent_vowel'},
    chr(70697) + chr(70715): {'char': 'mrr', 'type': 'consonant_dependent_vowel'},
    chr(70697) + chr(70716): {'char': 'ml', 'type': 'consonant_dependent_vowel'},
    chr(70697) + chr(70717): {'char': 'mll', 'type': 'consonant_dependent_vowel'},
    chr(70697) + chr(70718): {'char': 'me', 'type': 'consonant_dependent_vowel'},
    chr(70697) + chr(70719): {'char': 'mai', 'type': 'consonant_dependent_vowel'},
    chr(70697) + chr(70720): {'char': 'mo', 'type': 'consonant_dependent_vowel'},
    chr(70697) + chr(70721): {'char': 'mau', 'type': 'consonant_dependent_vowel'},


    # For `chr(70698)` (mh)
    chr(70698) + chr(70709): {'char': 'mha', 'type': 'consonant_dependent_vowel'},
    chr(70698) + chr(70710): {'char': 'mhi', 'type': 'consonant_dependent_vowel'},
    chr(70698) + chr(70711): {'char': 'mhii', 'type': 'consonant_dependent_vowel'},
    chr(70698) + chr(70712): {'char': 'mhu', 'type': 'consonant_dependent_vowel'},
    chr(70698) + chr(70713): {'char': 'mhuu', 'type': 'consonant_dependent_vowel'},
    chr(70698) + chr(70714): {'char': 'mhr', 'type': 'consonant_dependent_vowel'},
    chr(70698) + chr(70715): {'char': 'mhrr', 'type': 'consonant_dependent_vowel'},
    chr(70698) + chr(70716): {'char': 'mhl', 'type': 'consonant_dependent_vowel'},
    chr(70698) + chr(70717): {'char': 'mhll', 'type': 'consonant_dependent_vowel'},
    chr(70698) + chr(70718): {'char': 'mhe', 'type': 'consonant_dependent_vowel'},
    chr(70698) + chr(70719): {'char': 'mhai', 'type': 'consonant_dependent_vowel'},
    chr(70698) + chr(70720): {'char': 'mho', 'type': 'consonant_dependent_vowel'},
    chr(70698) + chr(70721): {'char': 'mhau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70699)` (y)
    chr(70699) + chr(70709): {'char': 'ya', 'type': 'consonant_dependent_vowel'},
    chr(70699) + chr(70710): {'char': 'yi', 'type': 'consonant_dependent_vowel'},
    chr(70699) + chr(70711): {'char': 'yii', 'type': 'consonant_dependent_vowel'},
    chr(70699) + chr(70712): {'char': 'yu', 'type': 'consonant_dependent_vowel'},
    chr(70699) + chr(70713): {'char': 'yuu', 'type': 'consonant_dependent_vowel'},
    chr(70699) + chr(70714): {'char': 'yr', 'type': 'consonant_dependent_vowel'},
    chr(70699) + chr(70715): {'char': 'yrr', 'type': 'consonant_dependent_vowel'},
    chr(70699) + chr(70716): {'char': 'yl', 'type': 'consonant_dependent_vowel'},
    chr(70699) + chr(70717): {'char': 'yll', 'type': 'consonant_dependent_vowel'},
    chr(70699) + chr(70718): {'char': 'ye', 'type': 'consonant_dependent_vowel'},
    chr(70699) + chr(70719): {'char': 'yai', 'type': 'consonant_dependent_vowel'},
    chr(70699) + chr(70720): {'char': 'yo', 'type': 'consonant_dependent_vowel'},
    chr(70699) + chr(70721): {'char': 'yau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70700)` (r)
    chr(70700) + chr(70709): {'char': 'ra', 'type': 'consonant_dependent_vowel'},
    chr(70700) + chr(70710): {'char': 'ri', 'type': 'consonant_dependent_vowel'},
    chr(70700) + chr(70711): {'char': 'rii', 'type': 'consonant_dependent_vowel'},
    chr(70700) + chr(70712): {'char': 'ru', 'type': 'consonant_dependent_vowel'},
    chr(70700) + chr(70713): {'char': 'ruu', 'type': 'consonant_dependent_vowel'},
    chr(70700) + chr(70714): {'char': 'rr', 'type': 'consonant_dependent_vowel'},
    chr(70700) + chr(70715): {'char': 'rrr', 'type': 'consonant_dependent_vowel'},
    chr(70700) + chr(70716): {'char': 'rl', 'type': 'consonant_dependent_vowel'},
    chr(70700) + chr(70717): {'char': 'rll', 'type': 'consonant_dependent_vowel'},
    chr(70700) + chr(70718): {'char': 're', 'type': 'consonant_dependent_vowel'},
    chr(70700) + chr(70719): {'char': 'rai', 'type': 'consonant_dependent_vowel'},
    chr(70700) + chr(70720): {'char': 'ro', 'type': 'consonant_dependent_vowel'},
    chr(70700) + chr(70721): {'char': 'rau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70701)` (rh)
    chr(70701) + chr(70709): {'char': 'rha', 'type': 'consonant_dependent_vowel'},
    chr(70701) + chr(70710): {'char': 'rhi', 'type': 'consonant_dependent_vowel'},
    chr(70701) + chr(70711): {'char': 'rhii', 'type': 'consonant_dependent_vowel'},
    chr(70701) + chr(70712): {'char': 'rhu', 'type': 'consonant_dependent_vowel'},
    chr(70701) + chr(70713): {'char': 'rhuu', 'type': 'consonant_dependent_vowel'},
    chr(70701) + chr(70714): {'char': 'rhr', 'type': 'consonant_dependent_vowel'},
    chr(70701) + chr(70715): {'char': 'rhrr', 'type': 'consonant_dependent_vowel'},
    chr(70701) + chr(70716): {'char': 'rhl', 'type': 'consonant_dependent_vowel'},
    chr(70701) + chr(70717): {'char': 'rhll', 'type': 'consonant_dependent_vowel'},
    chr(70701) + chr(70718): {'char': 'rhe', 'type': 'consonant_dependent_vowel'},
    chr(70701) + chr(70719): {'char': 'rhai', 'type': 'consonant_dependent_vowel'},
    chr(70701) + chr(70720): {'char': 'rho', 'type': 'consonant_dependent_vowel'},
    chr(70701) + chr(70721): {'char': 'rhau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70702)` (l)
    chr(70702) + chr(70709): {'char': 'la', 'type': 'consonant_dependent_vowel'},
    chr(70702) + chr(70710): {'char': 'li', 'type': 'consonant_dependent_vowel'},
    chr(70702) + chr(70711): {'char': 'lii', 'type': 'consonant_dependent_vowel'},
    chr(70702) + chr(70712): {'char': 'lu', 'type': 'consonant_dependent_vowel'},
    chr(70702) + chr(70713): {'char': 'luu', 'type': 'consonant_dependent_vowel'},
    chr(70702) + chr(70714): {'char': 'lr', 'type': 'consonant_dependent_vowel'},
    chr(70702) + chr(70715): {'char': 'lrr', 'type': 'consonant_dependent_vowel'},
    chr(70702) + chr(70716): {'char': 'll', 'type': 'consonant_dependent_vowel'},
    chr(70702) + chr(70717): {'char': 'lll', 'type': 'consonant_dependent_vowel'},
    chr(70702) + chr(70718): {'char': 'le', 'type': 'consonant_dependent_vowel'},
    chr(70702) + chr(70719): {'char': 'lai', 'type': 'consonant_dependent_vowel'},
    chr(70702) + chr(70720): {'char': 'lo', 'type': 'consonant_dependent_vowel'},
    chr(70702) + chr(70721): {'char': 'lau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70703)` (lh)
    chr(70703) + chr(70709): {'char': 'lha', 'type': 'consonant_dependent_vowel'},
    chr(70703) + chr(70710): {'char': 'lhi', 'type': 'consonant_dependent_vowel'},
    chr(70703) + chr(70711): {'char': 'lhii', 'type': 'consonant_dependent_vowel'},
    chr(70703) + chr(70712): {'char': 'lhu', 'type': 'consonant_dependent_vowel'},
    chr(70703) + chr(70713): {'char': 'lhuu', 'type': 'consonant_dependent_vowel'},
    chr(70703) + chr(70714): {'char': 'lhr', 'type': 'consonant_dependent_vowel'},
    chr(70703) + chr(70715): {'char': 'lhrr', 'type': 'consonant_dependent_vowel'},
    chr(70703) + chr(70716): {'char': 'lhl', 'type': 'consonant_dependent_vowel'},
    chr(70703) + chr(70717): {'char': 'lhll', 'type': 'consonant_dependent_vowel'},
    chr(70703) + chr(70718): {'char': 'lhe', 'type': 'consonant_dependent_vowel'},
    chr(70703) + chr(70719): {'char': 'lhai', 'type': 'consonant_dependent_vowel'},
    chr(70703) + chr(70720): {'char': 'lho', 'type': 'consonant_dependent_vowel'},
    chr(70703) + chr(70721): {'char': 'lhau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70704)` (w)
    chr(70704) + chr(70709): {'char': 'wa', 'type': 'consonant_dependent_vowel'},
    chr(70704) + chr(70710): {'char': 'wi', 'type': 'consonant_dependent_vowel'},
    chr(70704) + chr(70711): {'char': 'wii', 'type': 'consonant_dependent_vowel'},
    chr(70704) + chr(70712): {'char': 'wu', 'type': 'consonant_dependent_vowel'},
    chr(70704) + chr(70713): {'char': 'wuu', 'type': 'consonant_dependent_vowel'},
    chr(70704) + chr(70714): {'char': 'wr', 'type': 'consonant_dependent_vowel'},
    chr(70704) + chr(70715): {'char': 'wrr', 'type': 'consonant_dependent_vowel'},
    chr(70704) + chr(70716): {'char': 'wl', 'type': 'consonant_dependent_vowel'},
    chr(70704) + chr(70717): {'char': 'wll', 'type': 'consonant_dependent_vowel'},
    chr(70704) + chr(70718): {'char': 'we', 'type': 'consonant_dependent_vowel'},
    chr(70704) + chr(70719): {'char': 'wai', 'type': 'consonant_dependent_vowel'},
    chr(70704) + chr(70720): {'char': 'wo', 'type': 'consonant_dependent_vowel'},
    chr(70704) + chr(70721): {'char': 'wau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70705)` (sh)
    chr(70705) + chr(70709): {'char': 'sha', 'type': 'consonant_dependent_vowel'},
    chr(70705) + chr(70710): {'char': 'shi', 'type': 'consonant_dependent_vowel'},
    chr(70705) + chr(70711): {'char': 'shii', 'type': 'consonant_dependent_vowel'},
    chr(70705) + chr(70712): {'char': 'shu', 'type': 'consonant_dependent_vowel'},
    chr(70705) + chr(70713): {'char': 'shuu', 'type': 'consonant_dependent_vowel'},
    chr(70705) + chr(70714): {'char': 'shr', 'type': 'consonant_dependent_vowel'},
    chr(70705) + chr(70715): {'char': 'shrr', 'type': 'consonant_dependent_vowel'},
    chr(70705) + chr(70716): {'char': 'shl', 'type': 'consonant_dependent_vowel'},
    chr(70705) + chr(70717): {'char': 'shll', 'type': 'consonant_dependent_vowel'},
    chr(70705) + chr(70718): {'char': 'she', 'type': 'consonant_dependent_vowel'},
    chr(70705) + chr(70719): {'char': 'shai', 'type': 'consonant_dependent_vowel'},
    chr(70705) + chr(70720): {'char': 'sho', 'type': 'consonant_dependent_vowel'},
    chr(70705) + chr(70721): {'char': 'shau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70706)` (ss)
    chr(70706) + chr(70709): {'char': 'ssa', 'type': 'consonant_dependent_vowel'},
    chr(70706) + chr(70710): {'char': 'ssi', 'type': 'consonant_dependent_vowel'},
    chr(70706) + chr(70711): {'char': 'ssii', 'type': 'consonant_dependent_vowel'},
    chr(70706) + chr(70712): {'char': 'ssu', 'type': 'consonant_dependent_vowel'},
    chr(70706) + chr(70713): {'char': 'ssuu', 'type': 'consonant_dependent_vowel'},
    chr(70706) + chr(70714): {'char': 'ssr', 'type': 'consonant_dependent_vowel'},
    chr(70706) + chr(70715): {'char': 'ssrr', 'type': 'consonant_dependent_vowel'},
    chr(70706) + chr(70716): {'char': 'ssl', 'type': 'consonant_dependent_vowel'},
    chr(70706) + chr(70717): {'char': 'ssll', 'type': 'consonant_dependent_vowel'},
    chr(70706) + chr(70718): {'char': 'sse', 'type': 'consonant_dependent_vowel'},
    chr(70706) + chr(70719): {'char': 'ssai', 'type': 'consonant_dependent_vowel'},
    chr(70706) + chr(70720): {'char': 'sso', 'type': 'consonant_dependent_vowel'},
    chr(70706) + chr(70721): {'char': 'ssau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70707)` (s)
    chr(70707) + chr(70709): {'char': 'sa', 'type': 'consonant_dependent_vowel'},
    chr(70707) + chr(70710): {'char': 'si', 'type': 'consonant_dependent_vowel'},
    chr(70707) + chr(70711): {'char': 'sii', 'type': 'consonant_dependent_vowel'},
    chr(70707) + chr(70712): {'char': 'su', 'type': 'consonant_dependent_vowel'},
    chr(70707) + chr(70713): {'char': 'suu', 'type': 'consonant_dependent_vowel'},
    chr(70707) + chr(70714): {'char': 'sr', 'type': 'consonant_dependent_vowel'},
    chr(70707) + chr(70715): {'char': 'srr', 'type': 'consonant_dependent_vowel'},
    chr(70707) + chr(70716): {'char': 'sl', 'type': 'consonant_dependent_vowel'},
    chr(70707) + chr(70717): {'char': 'sll', 'type': 'consonant_dependent_vowel'},
    chr(70707) + chr(70718): {'char': 'se', 'type': 'consonant_dependent_vowel'},
    chr(70707) + chr(70719): {'char': 'sai', 'type': 'consonant_dependent_vowel'},
    chr(70707) + chr(70720): {'char': 'so', 'type': 'consonant_dependent_vowel'},
    chr(70707) + chr(70721): {'char': 'sau', 'type': 'consonant_dependent_vowel'},

    # For `chr(70708)` (h)
    chr(70708) + chr(70709): {'char': 'ha', 'type': 'consonant_dependent_vowel'},
    chr(70708) + chr(70710): {'char': 'hi', 'type': 'consonant_dependent_vowel'},
    chr(70708) + chr(70711): {'char': 'hii', 'type': 'consonant_dependent_vowel'},
    chr(70708) + chr(70712): {'char': 'hu', 'type': 'consonant_dependent_vowel'},
    chr(70708) + chr(70713): {'char': 'huu', 'type': 'consonant_dependent_vowel'},
    chr(70708) + chr(70714): {'char': 'hr', 'type': 'consonant_dependent_vowel'},
    chr(70708) + chr(70715): {'char': 'hrr', 'type': 'consonant_dependent_vowel'},
    chr(70708) + chr(70716): {'char': 'hl', 'type': 'consonant_dependent_vowel'},
    chr(70708) + chr(70717): {'char': 'hll', 'type': 'consonant_dependent_vowel'},
    chr(70708) + chr(70718): {'char': 'he', 'type': 'consonant_dependent_vowel'},
    chr(70708) + chr(70719): {'char': 'hai', 'type': 'consonant_dependent_vowel'},
    chr(70708) + chr(70720): {'char': 'ho', 'type': 'consonant_dependent_vowel'},
    chr(70708) + chr(70721): {'char': 'hau', 'type': 'consonant_dependent_vowel'},


    # Independent vowels followed by dependent vowels
    # Independent Vowels (a)
    chr(70656) + chr(70709): {'char': 'aa', 'type': 'independent_dependent_vowel'},
    chr(70656) + chr(70710): {'char': 'ai', 'type': 'independent_dependent_vowel'},
    chr(70656) + chr(70711): {'char': 'aii', 'type': 'independent_dependent_vowel'},
    chr(70656) + chr(70712): {'char': 'au', 'type': 'independent_dependent_vowel'},
    chr(70656) + chr(70713): {'char': 'auu', 'type': 'independent_dependent_vowel'},
    chr(70656) + chr(70714): {'char': 'ar', 'type': 'independent_dependent_vowel'},
    chr(70656) + chr(70715): {'char': 'arr', 'type': 'independent_dependent_vowel'},
    chr(70656) + chr(70716): {'char': 'al', 'type': 'independent_dependent_vowel'},
    chr(70656) + chr(70717): {'char': 'all', 'type': 'independent_dependent_vowel'},
    chr(70656) + chr(70718): {'char': 'ae', 'type': 'independent_dependent_vowel'},
    chr(70656) + chr(70719): {'char': 'aai', 'type': 'independent_dependent_vowel'},
    chr(70656) + chr(70720): {'char': 'ao', 'type': 'independent_dependent_vowel'},
    chr(70656) + chr(70721): {'char': 'au', 'type': 'independent_dependent_vowel'},

    # Independent Vowels (aa)
    chr(70657) + chr(70709): {'char': 'aaa', 'type': 'independent_dependent_vowel'},
    chr(70657) + chr(70710): {'char': 'aai', 'type': 'independent_dependent_vowel'},
    chr(70657) + chr(70711): {'char': 'aaii', 'type': 'independent_dependent_vowel'},
    chr(70657) + chr(70712): {'char': 'aau', 'type': 'independent_dependent_vowel'},
    chr(70657) + chr(70713): {'char': 'aauu', 'type': 'independent_dependent_vowel'},
    chr(70657) + chr(70714): {'char': 'aar', 'type': 'independent_dependent_vowel'},
    chr(70657) + chr(70715): {'char': 'aarr', 'type': 'independent_dependent_vowel'},
    chr(70657) + chr(70716): {'char': 'aal', 'type': 'independent_dependent_vowel'},
    chr(70657) + chr(70717): {'char': 'aall', 'type': 'independent_dependent_vowel'},
    chr(70657) + chr(70718): {'char': 'aae', 'type': 'independent_dependent_vowel'},
    chr(70657) + chr(70719): {'char': 'aai', 'type': 'independent_dependent_vowel'},
    chr(70657) + chr(70720): {'char': 'aao', 'type': 'independent_dependent_vowel'},
    chr(70657) + chr(70721): {'char': 'aau', 'type': 'independent_dependent_vowel'},

    # Independent Vowels (i)
    chr(70658) + chr(70709): {'char': 'ia', 'type': 'independent_dependent_vowel'},
    chr(70658) + chr(70710): {'char': 'ii', 'type': 'independent_dependent_vowel'},
    chr(70658) + chr(70711): {'char': 'iii', 'type': 'independent_dependent_vowel'},
    chr(70658) + chr(70712): {'char': 'iu', 'type': 'independent_dependent_vowel'},
    chr(70658) + chr(70713): {'char': 'iuu', 'type': 'independent_dependent_vowel'},
    chr(70658) + chr(70714): {'char': 'ir', 'type': 'independent_dependent_vowel'},
    chr(70658) + chr(70715): {'char': 'irr', 'type': 'independent_dependent_vowel'},
    chr(70658) + chr(70716): {'char': 'il', 'type': 'independent_dependent_vowel'},
    chr(70658) + chr(70717): {'char': 'ill', 'type': 'independent_dependent_vowel'},
    chr(70658) + chr(70718): {'char': 'ie', 'type': 'independent_dependent_vowel'},
    chr(70658) + chr(70719): {'char': 'iai', 'type': 'independent_dependent_vowel'},
    chr(70658) + chr(70720): {'char': 'io', 'type': 'independent_dependent_vowel'},
    chr(70658) + chr(70721): {'char': 'iau', 'type': 'independent_dependent_vowel'},

    # Independent Vowels (ii)
    chr(70659) + chr(70709): {'char': 'iia', 'type': 'independent_dependent_vowel'},
    chr(70659) + chr(70710): {'char': 'iii', 'type': 'independent_dependent_vowel'},
    chr(70659) + chr(70711): {'char': 'iiii', 'type': 'independent_dependent_vowel'},
    chr(70659) + chr(70712): {'char': 'iiu', 'type': 'independent_dependent_vowel'},
    chr(70659) + chr(70713): {'char': 'iiuu', 'type': 'independent_dependent_vowel'},
    chr(70659) + chr(70714): {'char': 'iir', 'type': 'independent_dependent_vowel'},
    chr(70659) + chr(70715): {'char': 'iirr', 'type': 'independent_dependent_vowel'},
    chr(70659) + chr(70716): {'char': 'iil', 'type': 'independent_dependent_vowel'},
    chr(70659) + chr(70717): {'char': 'iill', 'type': 'independent_dependent_vowel'},
    chr(70659) + chr(70718): {'char': 'iie', 'type': 'independent_dependent_vowel'},
    chr(70659) + chr(70719): {'char': 'iiai', 'type': 'independent_dependent_vowel'},
    chr(70659) + chr(70720): {'char': 'iio', 'type': 'independent_dependent_vowel'},
    chr(70659) + chr(70721): {'char': 'iiau', 'type': 'independent_dependent_vowel'},

    # Independent Vowels (u)
    chr(70660) + chr(70709): {'char': 'ua', 'type': 'independent_dependent_vowel'},
    chr(70660) + chr(70710): {'char': 'ui', 'type': 'independent_dependent_vowel'},
    chr(70660) + chr(70711): {'char': 'uii', 'type': 'independent_dependent_vowel'},
    chr(70660) + chr(70712): {'char': 'uu', 'type': 'independent_dependent_vowel'},
    chr(70660) + chr(70713): {'char': 'uuu', 'type': 'independent_dependent_vowel'},
    chr(70660) + chr(70714): {'char': 'ur', 'type': 'independent_dependent_vowel'},
    chr(70660) + chr(70715): {'char': 'urr', 'type': 'independent_dependent_vowel'},
    chr(70660) + chr(70716): {'char': 'ul', 'type': 'independent_dependent_vowel'},
    chr(70660) + chr(70717): {'char': 'ull', 'type': 'independent_dependent_vowel'},
    chr(70660) + chr(70718): {'char': 'ue', 'type': 'independent_dependent_vowel'},
    chr(70660) + chr(70719): {'char': 'uai', 'type': 'independent_dependent_vowel'},
    chr(70660) + chr(70720): {'char': 'uo', 'type': 'independent_dependent_vowel'},
    chr(70660) + chr(70721): {'char': 'uau', 'type': 'independent_dependent_vowel'},

    # Independent Vowels (uu)
    chr(70661) + chr(70709): {'char': 'uaa', 'type': 'independent_dependent_vowel'},
    chr(70661) + chr(70710): {'char': 'uui', 'type': 'independent_dependent_vowel'},
    chr(70661) + chr(70711): {'char': 'uuui', 'type': 'independent_dependent_vowel'},
    chr(70661) + chr(70712): {'char': 'uuu', 'type': 'independent_dependent_vowel'},
    chr(70661) + chr(70713): {'char': 'uuuu', 'type': 'independent_dependent_vowel'},
    chr(70661) + chr(70714): {'char': 'uur', 'type': 'independent_dependent_vowel'},
    chr(70661) + chr(70715): {'char': 'uurr', 'type': 'independent_dependent_vowel'},
    chr(70661) + chr(70716): {'char': 'uul', 'type': 'independent_dependent_vowel'},
    chr(70661) + chr(70717): {'char': 'uull', 'type': 'independent_dependent_vowel'},
    chr(70661) + chr(70718): {'char': 'uee', 'type': 'independent_dependent_vowel'},
    chr(70661) + chr(70719): {'char': 'uai', 'type': 'independent_dependent_vowel'},
    chr(70661) + chr(70720): {'char': 'uoo', 'type': 'independent_dependent_vowel'},
    chr(70661) + chr(70721): {'char': 'uau', 'type': 'independent_dependent_vowel'},

    # Independent Vowels (r)
    chr(70662) + chr(70709): {'char': 'ra', 'type': 'independent_dependent_vowel'},
    chr(70662) + chr(70710): {'char': 'ri', 'type': 'independent_dependent_vowel'},
    chr(70662) + chr(70711): {'char': 'rii', 'type': 'independent_dependent_vowel'},
    chr(70662) + chr(70712): {'char': 'ru', 'type': 'independent_dependent_vowel'},
    chr(70662) + chr(70713): {'char': 'ruu', 'type': 'independent_dependent_vowel'},
    chr(70662) + chr(70714): {'char': 'rr', 'type': 'independent_dependent_vowel'},
    chr(70662) + chr(70715): {'char': 'rrr', 'type': 'independent_dependent_vowel'},
    chr(70662) + chr(70716): {'char': 'rl', 'type': 'independent_dependent_vowel'},
    chr(70662) + chr(70717): {'char': 'rll', 'type': 'independent_dependent_vowel'},
    chr(70662) + chr(70718): {'char': 're', 'type': 'independent_dependent_vowel'},
    chr(70662) + chr(70719): {'char': 'rai', 'type': 'independent_dependent_vowel'},
    chr(70662) + chr(70720): {'char': 'ro', 'type': 'independent_dependent_vowel'},
    chr(70662) + chr(70721): {'char': 'rau', 'type': 'independent_dependent_vowel'},

    # Independent Vowels (rr)
    chr(70663) + chr(70709): {'char': 'rra', 'type': 'independent_dependent_vowel'},
    chr(70663) + chr(70710): {'char': 'rri', 'type': 'independent_dependent_vowel'},
    chr(70663) + chr(70711): {'char': 'rrrii', 'type': 'independent_dependent_vowel'},
    chr(70663) + chr(70712): {'char': 'rru', 'type': 'independent_dependent_vowel'},
    chr(70663) + chr(70713): {'char': 'rruu', 'type': 'independent_dependent_vowel'},
    chr(70663) + chr(70714): {'char': 'rrr', 'type': 'independent_dependent_vowel'},
    chr(70663) + chr(70715): {'char': 'rrrr', 'type': 'independent_dependent_vowel'},
    chr(70663) + chr(70716): {'char': 'rrl', 'type': 'independent_dependent_vowel'},
    chr(70663) + chr(70717): {'char': 'rrll', 'type': 'independent_dependent_vowel'},
    chr(70663) + chr(70718): {'char': 'rre', 'type': 'independent_dependent_vowel'},
    chr(70663) + chr(70719): {'char': 'rrai', 'type': 'independent_dependent_vowel'},
    chr(70663) + chr(70720): {'char': 'rro', 'type': 'independent_dependent_vowel'},
    chr(70663) + chr(70721): {'char': 'rrau', 'type': 'independent_dependent_vowel'},

    # Independent Vowels (l)
    chr(70664) + chr(70709): {'char': 'la', 'type': 'independent_dependent_vowel'},
    chr(70664) + chr(70710): {'char': 'li', 'type': 'independent_dependent_vowel'},
    chr(70664) + chr(70711): {'char': 'lii', 'type': 'independent_dependent_vowel'},
    chr(70664) + chr(70712): {'char': 'lu', 'type': 'independent_dependent_vowel'},
    chr(70664) + chr(70713): {'char': 'luu', 'type': 'independent_dependent_vowel'},
    chr(70664) + chr(70714): {'char': 'lr', 'type': 'independent_dependent_vowel'},
    chr(70664) + chr(70715): {'char': 'lrr', 'type': 'independent_dependent_vowel'},
    chr(70664) + chr(70716): {'char': 'll', 'type': 'independent_dependent_vowel'},
    chr(70664) + chr(70717): {'char': 'lll', 'type': 'independent_dependent_vowel'},
    chr(70664) + chr(70718): {'char': 'le', 'type': 'independent_dependent_vowel'},
    chr(70664) + chr(70719): {'char': 'lai', 'type': 'independent_dependent_vowel'},
    chr(70664) + chr(70720): {'char': 'lo', 'type': 'independent_dependent_vowel'},
    chr(70664) + chr(70721): {'char': 'lau', 'type': 'independent_dependent_vowel'},

    # Independent Vowels (ll)
    chr(70665) + chr(70709): {'char': 'lla', 'type': 'independent_dependent_vowel'},
    chr(70665) + chr(70710): {'char': 'lli', 'type': 'independent_dependent_vowel'},
    chr(70665) + chr(70711): {'char': 'llii', 'type': 'independent_dependent_vowel'},
    chr(70665) + chr(70712): {'char': 'llu', 'type': 'independent_dependent_vowel'},
    chr(70665) + chr(70713): {'char': 'lluu', 'type': 'independent_dependent_vowel'},
    chr(70665) + chr(70714): {'char': 'llr', 'type': 'independent_dependent_vowel'},
    chr(70665) + chr(70715): {'char': 'llrr', 'type': 'independent_dependent_vowel'},
    chr(70665) + chr(70716): {'char': 'lll', 'type': 'independent_dependent_vowel'},
    chr(70665) + chr(70717): {'char': 'llll', 'type': 'independent_dependent_vowel'},
    chr(70665) + chr(70718): {'char': 'lle', 'type': 'independent_dependent_vowel'},
    chr(70665) + chr(70719): {'char': 'llai', 'type': 'independent_dependent_vowel'},
    chr(70665) + chr(70720): {'char': 'llo', 'type': 'independent_dependent_vowel'},
    chr(70665) + chr(70721): {'char': 'llau', 'type': 'independent_dependent_vowel'},

    # Independent Vowels (e)
    chr(70666) + chr(70709): {'char': 'ea', 'type': 'independent_dependent_vowel'},
    chr(70666) + chr(70710): {'char': 'ei', 'type': 'independent_dependent_vowel'},
    chr(70666) + chr(70711): {'char': 'eii', 'type': 'independent_dependent_vowel'},
    chr(70666) + chr(70712): {'char': 'eu', 'type': 'independent_dependent_vowel'},
    chr(70666) + chr(70713): {'char': 'euu', 'type': 'independent_dependent_vowel'},
    chr(70666) + chr(70714): {'char': 'er', 'type': 'independent_dependent_vowel'},
    chr(70666) + chr(70715): {'char': 'err', 'type': 'independent_dependent_vowel'},
    chr(70666) + chr(70716): {'char': 'el', 'type': 'independent_dependent_vowel'},
    chr(70666) + chr(70717): {'char': 'ell', 'type': 'independent_dependent_vowel'},
    chr(70666) + chr(70718): {'char': 'ee', 'type': 'independent_dependent_vowel'},
    chr(70666) + chr(70719): {'char': 'eai', 'type': 'independent_dependent_vowel'},
    chr(70666) + chr(70720): {'char': 'eo', 'type': 'independent_dependent_vowel'},
    chr(70666) + chr(70721): {'char': 'eau', 'type': 'independent_dependent_vowel'},

    # Independent Vowels (ai)
    chr(70667) + chr(70709): {'char': 'aia', 'type': 'independent_dependent_vowel'},
    chr(70667) + chr(70710): {'char': 'aii', 'type': 'independent_dependent_vowel'},
    chr(70667) + chr(70711): {'char': 'aiii', 'type': 'independent_dependent_vowel'},
    chr(70667) + chr(70712): {'char': 'aiu', 'type': 'independent_dependent_vowel'},
    chr(70667) + chr(70713): {'char': 'aiuu', 'type': 'independent_dependent_vowel'},
    chr(70667) + chr(70714): {'char': 'air', 'type': 'independent_dependent_vowel'},
    chr(70667) + chr(70715): {'char': 'airr', 'type': 'independent_dependent_vowel'},
    chr(70667) + chr(70716): {'char': 'ail', 'type': 'independent_dependent_vowel'},
    chr(70667) + chr(70717): {'char': 'aill', 'type': 'independent_dependent_vowel'},
    chr(70667) + chr(70718): {'char': 'aie', 'type': 'independent_dependent_vowel'},
    chr(70667) + chr(70719): {'char': 'aiai', 'type': 'independent_dependent_vowel'},
    chr(70667) + chr(70720): {'char': 'aio', 'type': 'independent_dependent_vowel'},
    chr(70667) + chr(70721): {'char': 'aiau', 'type': 'independent_dependent_vowel'},

    # Independent Vowels (o)
    chr(70668) + chr(70709): {'char': 'oa', 'type': 'independent_dependent_vowel'},
    chr(70668) + chr(70710): {'char': 'oi', 'type': 'independent_dependent_vowel'},
    chr(70668) + chr(70711): {'char': 'oii', 'type': 'independent_dependent_vowel'},
    chr(70668) + chr(70712): {'char': 'ou', 'type': 'independent_dependent_vowel'},
    chr(70668) + chr(70713): {'char': 'ouu', 'type': 'independent_dependent_vowel'},
    chr(70668) + chr(70714): {'char': 'or', 'type': 'independent_dependent_vowel'},
    chr(70668) + chr(70715): {'char': 'orr', 'type': 'independent_dependent_vowel'},
    chr(70668) + chr(70716): {'char': 'ol', 'type': 'independent_dependent_vowel'},
    chr(70668) + chr(70717): {'char': 'oll', 'type': 'independent_dependent_vowel'},
    chr(70668) + chr(70718): {'char': 'oe', 'type': 'independent_dependent_vowel'},
    chr(70668) + chr(70719): {'char': 'oai', 'type': 'independent_dependent_vowel'},
    chr(70668) + chr(70720): {'char': 'oo', 'type': 'independent_dependent_vowel'},
    chr(70668) + chr(70721): {'char': 'oau', 'type': 'independent_dependent_vowel'},

    # Independent Vowels (au)
    chr(70669) + chr(70709): {'char': 'aua', 'type': 'independent_dependent_vowel'},
    chr(70669) + chr(70710): {'char': 'aui', 'type': 'independent_dependent_vowel'},
    chr(70669) + chr(70711): {'char': 'auii', 'type': 'independent_dependent_vowel'},
    chr(70669) + chr(70712): {'char': 'auu', 'type': 'independent_dependent_vowel'},
    chr(70669) + chr(70713): {'char': 'auuu', 'type': 'independent_dependent_vowel'},
    chr(70669) + chr(70714): {'char': 'aur', 'type': 'independent_dependent_vowel'},
    chr(70669) + chr(70715): {'char': 'aurr', 'type': 'independent_dependent_vowel'},
    chr(70669) + chr(70716): {'char': 'aul', 'type': 'independent_dependent_vowel'},
    chr(70669) + chr(70717): {'char': 'aull', 'type': 'independent_dependent_vowel'},
    chr(70669) + chr(70718): {'char': 'aue', 'type': 'independent_dependent_vowel'},
    chr(70669) + chr(70719): {'char': 'auai', 'type': 'independent_dependent_vowel'},
    chr(70669) + chr(70720): {'char': 'auo', 'type': 'independent_dependent_vowel'},
    chr(70669) + chr(70721): {'char': 'auau', 'type': 'independent_dependent_vowel'},


    #independent followed by symbols

    # Independent Vowels (a)
    chr(70656) + chr(70722): {'char': 'a', 'type': 'independent_symbol'},  # with virama
    chr(70656) + chr(70723): {'char': 'an', 'type': 'independent_symbol'},
    chr(70656) + chr(70724): {'char': 'am', 'type': 'independent_symbol'},
    chr(70656) + chr(70725): {'char': 'ah', 'type': 'independent_symbol'},
    chr(70656) + chr(70726): {'char': 'a', 'type': 'independent_symbol'},  # empty symbol
    chr(70656) + chr(70727): {'char': 'a', 'type': 'independent_symbol'},  # empty symbol
    chr(70656) + chr(70728): {'char': 'am', 'type': 'independent_symbol'},  # final anusvara
    chr(70656) + chr(70729): {'char': 'aom', 'type': 'independent_symbol'},
    chr(70656) + chr(70730): {'char': 'an', 'type': 'independent_symbol'},  # siddhi
    chr(70656) + chr(70747): {'char': 'a', 'type': 'independent_symbol'},  # placeholder mark
    chr(70656) + chr(70748): {'char': 'a', 'type': 'independent_symbol'},  # reserved
    chr(70656) + chr(70749): {'char': 'a', 'type': 'independent_symbol'},  # insertion sign
    chr(70656) + chr(70750): {'char': 'a', 'type': 'independent_symbol'},  # sandhi
    chr(70656) + chr(70751): {'char': 'am', 'type': 'independent_symbol'},  # vedic anusarva
    chr(70656) + chr(70752): {'char': 'at', 'type': 'independent_symbol'},  # jihvamuliya
    chr(70656) + chr(70753): {'char': 'an', 'type': 'independent_symbol'},  # upadhmaniya

    # Independent Vowels (aa)
    chr(70657) + chr(70722): {'char': 'aa', 'type': 'independent_symbol'},  # with virama
    chr(70657) + chr(70723): {'char': 'aan', 'type': 'independent_symbol'},
    chr(70657) + chr(70724): {'char': 'aam', 'type': 'independent_symbol'},
    chr(70657) + chr(70725): {'char': 'aah', 'type': 'independent_symbol'},
    chr(70657) + chr(70726): {'char': 'aa', 'type': 'independent_symbol'},  # empty symbol
    chr(70657) + chr(70727): {'char': 'aa', 'type': 'independent_symbol'},  # empty symbol
    chr(70657) + chr(70728): {'char': 'aam', 'type': 'independent_symbol'},  # final anusvara
    chr(70657) + chr(70729): {'char': 'aaom', 'type': 'independent_symbol'},
    chr(70657) + chr(70730): {'char': 'aan', 'type': 'independent_symbol'},  # siddhi
    chr(70657) + chr(70747): {'char': 'aa', 'type': 'independent_symbol'},  # placeholder mark
    chr(70657) + chr(70748): {'char': 'aa', 'type': 'independent_symbol'},  # reserved
    chr(70657) + chr(70749): {'char': 'aa', 'type': 'independent_symbol'},  # insertion sign
    chr(70657) + chr(70750): {'char': 'aa', 'type': 'independent_symbol'},  # sandhi
    chr(70657) + chr(70751): {'char': 'aam', 'type': 'independent_symbol'},  # vedic anusarva
    chr(70657) + chr(70752): {'char': 'aat', 'type': 'independent_symbol'},  # jihvamuliya
    chr(70657) + chr(70753): {'char': 'aan', 'type': 'independent_symbol'},  # upadhmaniya

    # Independent Vowels (i)
    chr(70658) + chr(70722): {'char': 'i', 'type': 'independent_symbol'},  # with virama
    chr(70658) + chr(70723): {'char': 'in', 'type': 'independent_symbol'},
    chr(70658) + chr(70724): {'char': 'im', 'type': 'independent_symbol'},
    chr(70658) + chr(70725): {'char': 'ih', 'type': 'independent_symbol'},
    chr(70658) + chr(70726): {'char': 'i', 'type': 'independent_symbol'},  # empty symbol
    chr(70658) + chr(70727): {'char': 'i', 'type': 'independent_symbol'},  # empty symbol
    chr(70658) + chr(70728): {'char': 'im', 'type': 'independent_symbol'},  # final anusvara
    chr(70658) + chr(70729): {'char': 'iom', 'type': 'independent_symbol'},
    chr(70658) + chr(70730): {'char': 'in', 'type': 'independent_symbol'},  # siddhi
    chr(70658) + chr(70747): {'char': 'i', 'type': 'independent_symbol'},  # placeholder mark
    chr(70658) + chr(70748): {'char': 'i', 'type': 'independent_symbol'},  # reserved
    chr(70658) + chr(70749): {'char': 'i', 'type': 'independent_symbol'},  # insertion sign
    chr(70658) + chr(70750): {'char': 'i', 'type': 'independent_symbol'},  # sandhi
    chr(70658) + chr(70751): {'char': 'im', 'type': 'independent_symbol'},  # vedic anusarva
    chr(70658) + chr(70752): {'char': 'it', 'type': 'independent_symbol'},  # jihvamuliya
    chr(70658) + chr(70753): {'char': 'in', 'type': 'independent_symbol'},  # upadhmaniya

    # Independent Vowels (ii)
    chr(70659) + chr(70722): {'char': 'ii', 'type': 'independent_symbol'},  # with virama
    chr(70659) + chr(70723): {'char': 'iin', 'type': 'independent_symbol'},
    chr(70659) + chr(70724): {'char': 'iim', 'type': 'independent_symbol'},
    chr(70659) + chr(70725): {'char': 'iih', 'type': 'independent_symbol'},
    chr(70659) + chr(70726): {'char': 'ii', 'type': 'independent_symbol'},  # empty symbol
    chr(70659) + chr(70727): {'char': 'ii', 'type': 'independent_symbol'},  # empty symbol
    chr(70659) + chr(70728): {'char': 'iim', 'type': 'independent_symbol'},  # final anusvara
    chr(70659) + chr(70729): {'char': 'iiom', 'type': 'independent_symbol'},
    chr(70659) + chr(70730): {'char': 'iin', 'type': 'independent_symbol'},  # siddhi
    chr(70659) + chr(70747): {'char': 'ii', 'type': 'independent_symbol'},  # placeholder mark
    chr(70659) + chr(70748): {'char': 'ii', 'type': 'independent_symbol'},  # reserved
    chr(70659) + chr(70749): {'char': 'ii', 'type': 'independent_symbol'},  # insertion sign
    chr(70659) + chr(70750): {'char': 'ii', 'type': 'independent_symbol'},  # sandhi
    chr(70659) + chr(70751): {'char': 'iim', 'type': 'independent_symbol'},  # vedic anusarva
    chr(70659) + chr(70752): {'char': 'iit', 'type': 'independent_symbol'},  # jihvamuliya
    chr(70659) + chr(70753): {'char': 'iin', 'type': 'independent_symbol'},  # upadhmaniya

    # Independent Vowels (u)
    chr(70660) + chr(70722): {'char': 'u', 'type': 'independent_symbol'},  # with virama
    chr(70660) + chr(70723): {'char': 'un', 'type': 'independent_symbol'},
    chr(70660) + chr(70724): {'char': 'um', 'type': 'independent_symbol'},
    chr(70660) + chr(70725): {'char': 'uh', 'type': 'independent_symbol'},
    chr(70660) + chr(70726): {'char': 'u', 'type': 'independent_symbol'},  # empty symbol
    chr(70660) + chr(70727): {'char': 'u', 'type': 'independent_symbol'},  # empty symbol
    chr(70660) + chr(70728): {'char': 'um', 'type': 'independent_symbol'},  # final anusvara
    chr(70660) + chr(70729): {'char': 'uom', 'type': 'independent_symbol'},
    chr(70660) + chr(70730): {'char': 'un', 'type': 'independent_symbol'},  # siddhi
    chr(70660) + chr(70747): {'char': 'u', 'type': 'independent_symbol'},  # placeholder mark
    chr(70660) + chr(70748): {'char': 'u', 'type': 'independent_symbol'},  # reserved
    chr(70660) + chr(70749): {'char': 'u', 'type': 'independent_symbol'},  # insertion sign
    chr(70660) + chr(70750): {'char': 'u', 'type': 'independent_symbol'},  # sandhi
    chr(70660) + chr(70751): {'char': 'um', 'type': 'independent_symbol'},  # vedic anusarva
    chr(70660) + chr(70752): {'char': 'ut', 'type': 'independent_symbol'},  # jihvamuliya
    chr(70660) + chr(70753): {'char': 'un', 'type': 'independent_symbol'},  # upadhmaniya

    # Independent Vowels (uu)
    chr(70661) + chr(70722): {'char': 'uu', 'type': 'independent_symbol'},  # with virama
    chr(70661) + chr(70723): {'char': 'uun', 'type': 'independent_symbol'},
    chr(70661) + chr(70724): {'char': 'uum', 'type': 'independent_symbol'},
    chr(70661) + chr(70725): {'char': 'uuh', 'type': 'independent_symbol'},
    chr(70661) + chr(70726): {'char': 'uu', 'type': 'independent_symbol'},  # empty symbol
    chr(70661) + chr(70727): {'char': 'uu', 'type': 'independent_symbol'},  # empty symbol
    chr(70661) + chr(70728): {'char': 'uum', 'type': 'independent_symbol'},  # final anusvara
    chr(70661) + chr(70729): {'char': 'uuom', 'type': 'independent_symbol'},
    chr(70661) + chr(70730): {'char': 'uun', 'type': 'independent_symbol'},  # siddhi
    chr(70661) + chr(70747): {'char': 'uu', 'type': 'independent_symbol'},  # placeholder mark
    chr(70661) + chr(70748): {'char': 'uu', 'type': 'independent_symbol'},  # reserved
    chr(70661) + chr(70749): {'char': 'uu', 'type': 'independent_symbol'},  # insertion sign
    chr(70661) + chr(70750): {'char': 'uu', 'type': 'independent_symbol'},  # sandhi
    chr(70661) + chr(70751): {'char': 'uum', 'type': 'independent_symbol'},  # vedic anusarva
    chr(70661) + chr(70752): {'char': 'uut', 'type': 'independent_symbol'},  # jihvamuliya
    chr(70661) + chr(70753): {'char': 'uun', 'type': 'independent_symbol'},  # upadhmaniya

    # Independent Vowels (r)
    chr(70662) + chr(70722): {'char': 'r', 'type': 'independent_symbol'},  # with virama
    chr(70662) + chr(70723): {'char': 'rn', 'type': 'independent_symbol'},
    chr(70662) + chr(70724): {'char': 'rm', 'type': 'independent_symbol'},
    chr(70662) + chr(70725): {'char': 'rh', 'type': 'independent_symbol'},
    chr(70662) + chr(70726): {'char': 'r', 'type': 'independent_symbol'},  # empty symbol
    chr(70662) + chr(70727): {'char': 'r', 'type': 'independent_symbol'},  # empty symbol
    chr(70662) + chr(70728): {'char': 'rm', 'type': 'independent_symbol'},  # final anusvara
    chr(70662) + chr(70729): {'char': 'rom', 'type': 'independent_symbol'},
    chr(70662) + chr(70730): {'char': 'rn', 'type': 'independent_symbol'},  # siddhi
    chr(70662) + chr(70747): {'char': 'r', 'type': 'independent_symbol'},  # placeholder mark
    chr(70662) + chr(70748): {'char': 'r', 'type': 'independent_symbol'},  # reserved
    chr(70662) + chr(70749): {'char': 'r', 'type': 'independent_symbol'},  # insertion sign
    chr(70662) + chr(70750): {'char': 'r', 'type': 'independent_symbol'},  # sandhi
    chr(70662) + chr(70751): {'char': 'rm', 'type': 'independent_symbol'},  # vedic anusarva
    chr(70662) + chr(70752): {'char': 'rt', 'type': 'independent_symbol'},  # jihvamuliya
    chr(70662) + chr(70753): {'char': 'rn', 'type': 'independent_symbol'},  # upadhmaniya

    # Independent Vowels (rr)
    chr(70663) + chr(70722): {'char': 'rr', 'type': 'independent_symbol'},  # with virama
    chr(70663) + chr(70723): {'char': 'rrn', 'type': 'independent_symbol'},
    chr(70663) + chr(70724): {'char': 'rrm', 'type': 'independent_symbol'},
    chr(70663) + chr(70725): {'char': 'rrh', 'type': 'independent_symbol'},
    chr(70663) + chr(70726): {'char': 'rr', 'type': 'independent_symbol'},  # empty symbol
    chr(70663) + chr(70727): {'char': 'rr', 'type': 'independent_symbol'},  # empty symbol
    chr(70663) + chr(70728): {'char': 'rrm', 'type': 'independent_symbol'},  # final anusvara
    chr(70663) + chr(70729): {'char': 'rrom', 'type': 'independent_symbol'},
    chr(70663) + chr(70730): {'char': 'rrn', 'type': 'independent_symbol'},  # siddhi
    chr(70663) + chr(70747): {'char': 'rr', 'type': 'independent_symbol'},  # placeholder mark
    chr(70663) + chr(70748): {'char': 'rr', 'type': 'independent_symbol'},  # reserved
    chr(70663) + chr(70749): {'char': 'rr', 'type': 'independent_symbol'},  # insertion sign
    chr(70663) + chr(70750): {'char': 'rr', 'type': 'independent_symbol'},  # sandhi
    chr(70663) + chr(70751): {'char': 'rrm', 'type': 'independent_symbol'},  # vedic anusarva
    chr(70663) + chr(70752): {'char': 'rrt', 'type': 'independent_symbol'},  # jihvamuliya
    chr(70663) + chr(70753): {'char': 'rrn', 'type': 'independent_symbol'},  # upadhmaniya

    # Independent Vowels (l)
    chr(70664) + chr(70722): {'char': 'l', 'type': 'independent_symbol'},  # with virama
    chr(70664) + chr(70723): {'char': 'ln', 'type': 'independent_symbol'},
    chr(70664) + chr(70724): {'char': 'lm', 'type': 'independent_symbol'},
    chr(70664) + chr(70725): {'char': 'lh', 'type': 'independent_symbol'},
    chr(70664) + chr(70726): {'char': 'l', 'type': 'independent_symbol'},  # empty symbol
    chr(70664) + chr(70727): {'char': 'l', 'type': 'independent_symbol'},  # empty symbol
    chr(70664) + chr(70728): {'char': 'lm', 'type': 'independent_symbol'},  # final anusvara
    chr(70664) + chr(70729): {'char': 'lom', 'type': 'independent_symbol'},
    chr(70664) + chr(70730): {'char': 'ln', 'type': 'independent_symbol'},  # siddhi
    chr(70664) + chr(70747): {'char': 'l', 'type': 'independent_symbol'},  # placeholder mark
    chr(70664) + chr(70748): {'char': 'l', 'type': 'independent_symbol'},  # reserved
    chr(70664) + chr(70749): {'char': 'l', 'type': 'independent_symbol'},  # insertion sign
    chr(70664) + chr(70750): {'char': 'l', 'type': 'independent_symbol'},  # sandhi
    chr(70664) + chr(70751): {'char': 'lm', 'type': 'independent_symbol'},  # vedic anusarva
    chr(70664) + chr(70752): {'char': 'lt', 'type': 'independent_symbol'},  # jihvamuliya
    chr(70664) + chr(70753): {'char': 'ln', 'type': 'independent_symbol'},  # upadhmaniya

    # Independent Vowels (ll)
    chr(70665) + chr(70722): {'char': 'll', 'type': 'independent_symbol'},  # with virama
    chr(70665) + chr(70723): {'char': 'lln', 'type': 'independent_symbol'},
    chr(70665) + chr(70724): {'char': 'llm', 'type': 'independent_symbol'},
    chr(70665) + chr(70725): {'char': 'llh', 'type': 'independent_symbol'},
    chr(70665) + chr(70726): {'char': 'll', 'type': 'independent_symbol'},  # empty symbol
    chr(70665) + chr(70727): {'char': 'll', 'type': 'independent_symbol'},  # empty symbol
    chr(70665) + chr(70728): {'char': 'llm', 'type': 'independent_symbol'},  # final anusvara
    chr(70665) + chr(70729): {'char': 'llom', 'type': 'independent_symbol'},
    chr(70665) + chr(70730): {'char': 'lln', 'type': 'independent_symbol'},  # siddhi
    chr(70665) + chr(70747): {'char': 'll', 'type': 'independent_symbol'},  # placeholder mark
    chr(70665) + chr(70748): {'char': 'll', 'type': 'independent_symbol'},  # reserved
    chr(70665) + chr(70749): {'char': 'll', 'type': 'independent_symbol'},  # insertion sign
    chr(70665) + chr(70750): {'char': 'll', 'type': 'independent_symbol'},  # sandhi
    chr(70665) + chr(70751): {'char': 'llm', 'type': 'independent_symbol'},  # vedic anusarva
    chr(70665) + chr(70752): {'char': 'llt', 'type': 'independent_symbol'},  # jihvamuliya
    chr(70665) + chr(70753): {'char': 'lln', 'type': 'independent_symbol'},  # upadhmaniya

    # Independent Vowels (e)
    chr(70666) + chr(70722): {'char': 'e', 'type': 'independent_symbol'},  # with virama
    chr(70666) + chr(70723): {'char': 'en', 'type': 'independent_symbol'},
    chr(70666) + chr(70724): {'char': 'em', 'type': 'independent_symbol'},
    chr(70666) + chr(70725): {'char': 'eh', 'type': 'independent_symbol'},
    chr(70666) + chr(70726): {'char': 'e', 'type': 'independent_symbol'},  # empty symbol
    chr(70666) + chr(70727): {'char': 'e', 'type': 'independent_symbol'},  # empty symbol
    chr(70666) + chr(70728): {'char': 'em', 'type': 'independent_symbol'},  # final anusvara
    chr(70666) + chr(70729): {'char': 'eom', 'type': 'independent_symbol'},
    chr(70666) + chr(70730): {'char': 'en', 'type': 'independent_symbol'},  # siddhi
    chr(70666) + chr(70747): {'char': 'e', 'type': 'independent_symbol'},  # placeholder mark
    chr(70666) + chr(70748): {'char': 'e', 'type': 'independent_symbol'},  # reserved
    chr(70666) + chr(70749): {'char': 'e', 'type': 'independent_symbol'},  # insertion sign
    chr(70666) + chr(70750): {'char': 'e', 'type': 'independent_symbol'},  # sandhi
    chr(70666) + chr(70751): {'char': 'em', 'type': 'independent_symbol'},  # vedic anusarva
    chr(70666) + chr(70752): {'char': 'et', 'type': 'independent_symbol'},  # jihvamuliya
    chr(70666) + chr(70753): {'char': 'en', 'type': 'independent_symbol'},  # upadhmaniya

    # Independent Vowels (ai)
    chr(70667) + chr(70722): {'char': 'ai', 'type': 'independent_symbol'},  # with virama
    chr(70667) + chr(70723): {'char': 'ain', 'type': 'independent_symbol'},
    chr(70667) + chr(70724): {'char': 'aim', 'type': 'independent_symbol'},
    chr(70667) + chr(70725): {'char': 'aih', 'type': 'independent_symbol'},
    chr(70667) + chr(70726): {'char': 'ai', 'type': 'independent_symbol'},  # empty symbol
    chr(70667) + chr(70727): {'char': 'ai', 'type': 'independent_symbol'},  # empty symbol
    chr(70667) + chr(70728): {'char': 'aim', 'type': 'independent_symbol'},  # final anusvara
    chr(70667) + chr(70729): {'char': 'aiom', 'type': 'independent_symbol'},
    chr(70667) + chr(70730): {'char': 'ain', 'type': 'independent_symbol'},  # siddhi
    chr(70667) + chr(70747): {'char': 'ai', 'type': 'independent_symbol'},  # placeholder mark
    chr(70667) + chr(70748): {'char': 'ai', 'type': 'independent_symbol'},  # reserved
    chr(70667) + chr(70749): {'char': 'ai', 'type': 'independent_symbol'},  # insertion sign
    chr(70667) + chr(70750): {'char': 'ai', 'type': 'independent_symbol'},  # sandhi
    chr(70667) + chr(70751): {'char': 'aim', 'type': 'independent_symbol'},  # vedic anusarva
    chr(70667) + chr(70752): {'char': 'ait', 'type': 'independent_symbol'},  # jihvamuliya
    chr(70667) + chr(70753): {'char': 'ain', 'type': 'independent_symbol'},  # upadhmaniya

    # Independent Vowels (o)
    chr(70668) + chr(70722): {'char': 'o', 'type': 'independent_symbol'},  # with virama
    chr(70668) + chr(70723): {'char': 'on', 'type': 'independent_symbol'},
    chr(70668) + chr(70724): {'char': 'om', 'type': 'independent_symbol'},
    chr(70668) + chr(70725): {'char': 'oh', 'type': 'independent_symbol'},
    chr(70668) + chr(70726): {'char': 'o', 'type': 'independent_symbol'},  # empty symbol
    chr(70668) + chr(70727): {'char': 'o', 'type': 'independent_symbol'},  # empty symbol
    chr(70668) + chr(70728): {'char': 'om', 'type': 'independent_symbol'},  # final anusvara
    chr(70668) + chr(70729): {'char': 'oom', 'type': 'independent_symbol'},
    chr(70668) + chr(70730): {'char': 'on', 'type': 'independent_symbol'},  # siddhi
    chr(70668) + chr(70747): {'char': 'o', 'type': 'independent_symbol'},  # placeholder mark
    chr(70668) + chr(70748): {'char': 'o', 'type': 'independent_symbol'},  # reserved
    chr(70668) + chr(70749): {'char': 'o', 'type': 'independent_symbol'},  # insertion sign
    chr(70668) + chr(70750): {'char': 'o', 'type': 'independent_symbol'},  # sandhi
    chr(70668) + chr(70751): {'char': 'om', 'type': 'independent_symbol'},  # vedic anusarva
    chr(70668) + chr(70752): {'char': 'ot', 'type': 'independent_symbol'},  # jihvamuliya
    chr(70668) + chr(70753): {'char': 'on', 'type': 'independent_symbol'},  # upadhmaniya

    # Independent Vowels (au)
    chr(70669) + chr(70722): {'char': 'au', 'type': 'independent_symbol'},  # with virama
    chr(70669) + chr(70723): {'char': 'aun', 'type': 'independent_symbol'},
    chr(70669) + chr(70724): {'char': 'aum', 'type': 'independent_symbol'},
    chr(70669) + chr(70725): {'char': 'auh', 'type': 'independent_symbol'},
    chr(70669) + chr(70726): {'char': 'au', 'type': 'independent_symbol'},  # empty symbol
    chr(70669) + chr(70727): {'char': 'au', 'type': 'independent_symbol'},  # empty symbol
    chr(70669) + chr(70728): {'char': 'aum', 'type': 'independent_symbol'},  # final anusvara
    chr(70669) + chr(70729): {'char': 'auom', 'type': 'independent_symbol'},
    chr(70669) + chr(70730): {'char': 'aun', 'type': 'independent_symbol'},  # siddhi
    chr(70669) + chr(70747): {'char': 'au', 'type': 'independent_symbol'},  # placeholder mark
    chr(70669) + chr(70748): {'char': 'au', 'type': 'independent_symbol'},  # reserved
    chr(70669) + chr(70749): {'char': 'au', 'type': 'independent_symbol'},  # insertion sign
    chr(70669) + chr(70750): {'char': 'au', 'type': 'independent_symbol'},  # sandhi
    chr(70669) + chr(70751): {'char': 'aum', 'type': 'independent_symbol'},  # vedic anusarva
    chr(70669) + chr(70752): {'char': 'aut', 'type': 'independent_symbol'},  # jihvamuliya
    chr(70669) + chr(70753): {'char': 'aun', 'type': 'independent_symbol'},  # upadhmaniya


    chr(70670) + chr(70722): {'char': 'k', 'type': 'consonant_symbol'},  # with virama
    chr(70670) + chr(70723): {'char': 'kn', 'type': 'consonant_symbol'},
    chr(70670) + chr(70724): {'char': 'km', 'type': 'consonant_symbol'},
    chr(70670) + chr(70725): {'char': 'kh', 'type': 'consonant_symbol'},
    chr(70670) + chr(70726): {'char': 'k', 'type': 'consonant_symbol'},  # empty symbol
    chr(70670) + chr(70727): {'char': 'k', 'type': 'consonant_symbol'},  # empty symbol
    chr(70670) + chr(70728): {'char': 'km', 'type': 'consonant_symbol'},  # final anusvara
    chr(70670) + chr(70729): {'char': 'kom', 'type': 'consonant_symbol'},
    chr(70670) + chr(70730): {'char': 'kn', 'type': 'consonant_symbol'},  # siddhi
    chr(70670) + chr(70747): {'char': 'k', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70670) + chr(70748): {'char': 'k', 'type': 'consonant_symbol'},  # reserved
    chr(70670) + chr(70749): {'char': 'k', 'type': 'consonant_symbol'},  # insertion sign
    chr(70670) + chr(70750): {'char': 'k', 'type': 'consonant_symbol'},  # sandhi
    chr(70670) + chr(70751): {'char': 'km', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70670) + chr(70752): {'char': 'kt', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70670) + chr(70753): {'char': 'kn', 'type': 'consonant_symbol'},  # upadhmaniya

    # kh
    chr(70671) + chr(70722): {'char': 'kh', 'type': 'consonant_symbol'},  # with virama
    chr(70671) + chr(70723): {'char': 'khn', 'type': 'consonant_symbol'},
    chr(70671) + chr(70724): {'char': 'khm', 'type': 'consonant_symbol'},
    chr(70671) + chr(70725): {'char': 'khh', 'type': 'consonant_symbol'},
    chr(70671) + chr(70726): {'char': 'kh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70671) + chr(70727): {'char': 'kh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70671) + chr(70728): {'char': 'khm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70671) + chr(70729): {'char': 'khom', 'type': 'consonant_symbol'},
    chr(70671) + chr(70730): {'char': 'khn', 'type': 'consonant_symbol'},  # siddhi
    chr(70671) + chr(70747): {'char': 'kh', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70671) + chr(70748): {'char': 'kh', 'type': 'consonant_symbol'},  # reserved
    chr(70671) + chr(70749): {'char': 'kh', 'type': 'consonant_symbol'},  # insertion sign
    chr(70671) + chr(70750): {'char': 'kh', 'type': 'consonant_symbol'},  # sandhi
    chr(70671) + chr(70751): {'char': 'khm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70671) + chr(70752): {'char': 'kht', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70671) + chr(70753): {'char': 'khn', 'type': 'consonant_symbol'},  # upadhmaniya

    # g
    chr(70672) + chr(70722): {'char': 'g', 'type': 'consonant_symbol'},  # with virama
    chr(70672) + chr(70723): {'char': 'gn', 'type': 'consonant_symbol'},
    chr(70672) + chr(70724): {'char': 'gm', 'type': 'consonant_symbol'},
    chr(70672) + chr(70725): {'char': 'gh', 'type': 'consonant_symbol'},
    chr(70672) + chr(70726): {'char': 'g', 'type': 'consonant_symbol'},  # empty symbol
    chr(70672) + chr(70727): {'char': 'g', 'type': 'consonant_symbol'},  # empty symbol
    chr(70672) + chr(70728): {'char': 'gm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70672) + chr(70729): {'char': 'gom', 'type': 'consonant_symbol'},
    chr(70672) + chr(70730): {'char': 'gn', 'type': 'consonant_symbol'},  # siddhi
    chr(70672) + chr(70747): {'char': 'g', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70672) + chr(70748): {'char': 'g', 'type': 'consonant_symbol'},  # reserved
    chr(70672) + chr(70749): {'char': 'g', 'type': 'consonant_symbol'},  # insertion sign
    chr(70672) + chr(70750): {'char': 'g', 'type': 'consonant_symbol'},  # sandhi
    chr(70672) + chr(70751): {'char': 'gm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70672) + chr(70752): {'char': 'gt', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70672) + chr(70753): {'char': 'gn', 'type': 'consonant_symbol'},  # upadhmaniya

    # gh
    chr(70673) + chr(70722): {'char': 'gh', 'type': 'consonant_symbol'},  # with virama
    chr(70673) + chr(70723): {'char': 'ghn', 'type': 'consonant_symbol'},
    chr(70673) + chr(70724): {'char': 'ghm', 'type': 'consonant_symbol'},
    chr(70673) + chr(70725): {'char': 'ghh', 'type': 'consonant_symbol'},
    chr(70673) + chr(70726): {'char': 'gh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70673) + chr(70727): {'char': 'gh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70673) + chr(70728): {'char': 'ghm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70673) + chr(70729): {'char': 'ghom', 'type': 'consonant_symbol'},
    chr(70673) + chr(70730): {'char': 'ghn', 'type': 'consonant_symbol'},  # siddhi
    chr(70673) + chr(70747): {'char': 'gh', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70673) + chr(70748): {'char': 'gh', 'type': 'consonant_symbol'},  # reserved
    chr(70673) + chr(70749): {'char': 'gh', 'type': 'consonant_symbol'},  # insertion sign
    chr(70673) + chr(70750): {'char': 'gh', 'type': 'consonant_symbol'},  # sandhi
    chr(70673) + chr(70751): {'char': 'ghm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70673) + chr(70752): {'char': 'ght', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70673) + chr(70753): {'char': 'ghn', 'type': 'consonant_symbol'},  # upadhmaniya

    # ng
    chr(70674) + chr(70722): {'char': 'ng', 'type': 'consonant_symbol'},  # with virama
    chr(70674) + chr(70723): {'char': 'ngn', 'type': 'consonant_symbol'},
    chr(70674) + chr(70724): {'char': 'ngm', 'type': 'consonant_symbol'},
    chr(70674) + chr(70725): {'char': 'ngh', 'type': 'consonant_symbol'},
    chr(70674) + chr(70726): {'char': 'ng', 'type': 'consonant_symbol'},  # empty symbol
    chr(70674) + chr(70727): {'char': 'ng', 'type': 'consonant_symbol'},  # empty symbol
    chr(70674) + chr(70728): {'char': 'ngm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70674) + chr(70729): {'char': 'ngom', 'type': 'consonant_symbol'},
    chr(70674) + chr(70730): {'char': 'ngn', 'type': 'consonant_symbol'},  # siddhi
    chr(70674) + chr(70747): {'char': 'ng', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70674) + chr(70748): {'char': 'ng', 'type': 'consonant_symbol'},  # reserved
    chr(70674) + chr(70749): {'char': 'ng', 'type': 'consonant_symbol'},  # insertion sign
    chr(70674) + chr(70750): {'char': 'ng', 'type': 'consonant_symbol'},  # sandhi
    chr(70674) + chr(70751): {'char': 'ngm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70674) + chr(70752): {'char': 'ngt', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70674) + chr(70753): {'char': 'ngn', 'type': 'consonant_symbol'},  # upadhmaniya

    # ngh
    chr(70675) + chr(70722): {'char': 'ngh', 'type': 'consonant_symbol'},  # with virama
    chr(70675) + chr(70723): {'char': 'nghn', 'type': 'consonant_symbol'},
    chr(70675) + chr(70724): {'char': 'nghm', 'type': 'consonant_symbol'},
    chr(70675) + chr(70725): {'char': 'nghh', 'type': 'consonant_symbol'},
    chr(70675) + chr(70726): {'char': 'ngh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70675) + chr(70727): {'char': 'ngh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70675) + chr(70728): {'char': 'nghm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70675) + chr(70729): {'char': 'nghom', 'type': 'consonant_symbol'},
    chr(70675) + chr(70730): {'char': 'nghn', 'type': 'consonant_symbol'},  # siddhi
    chr(70675) + chr(70747): {'char': 'ngh', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70675) + chr(70748): {'char': 'ngh', 'type': 'consonant_symbol'},  # reserved
    chr(70675) + chr(70749): {'char': 'ngh', 'type': 'consonant_symbol'},  # insertion sign
    chr(70675) + chr(70750): {'char': 'ngh', 'type': 'consonant_symbol'},  # sandhi
    chr(70675) + chr(70751): {'char': 'nghm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70675) + chr(70752): {'char': 'nght', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70675) + chr(70753): {'char': 'nghn', 'type': 'consonant_symbol'},  # upadhmaniya

    # ch
    chr(70676) + chr(70722): {'char': 'ch', 'type': 'consonant_symbol'},  # with virama
    chr(70676) + chr(70723): {'char': 'chn', 'type': 'consonant_symbol'},
    chr(70676) + chr(70724): {'char': 'chm', 'type': 'consonant_symbol'},
    chr(70676) + chr(70725): {'char': 'chh', 'type': 'consonant_symbol'},
    chr(70676) + chr(70726): {'char': 'ch', 'type': 'consonant_symbol'},  # empty symbol
    chr(70676) + chr(70727): {'char': 'ch', 'type': 'consonant_symbol'},  # empty symbol
    chr(70676) + chr(70728): {'char': 'chm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70676) + chr(70729): {'char': 'chom', 'type': 'consonant_symbol'},
    chr(70676) + chr(70730): {'char': 'chn', 'type': 'consonant_symbol'},  # siddhi
    chr(70676) + chr(70747): {'char': 'ch', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70676) + chr(70748): {'char': 'ch', 'type': 'consonant_symbol'},  # reserved
    chr(70676) + chr(70749): {'char': 'ch', 'type': 'consonant_symbol'},  # insertion sign
    chr(70676) + chr(70750): {'char': 'ch', 'type': 'consonant_symbol'},  # sandhi
    chr(70676) + chr(70751): {'char': 'chm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70676) + chr(70752): {'char': 'cht', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70676) + chr(70753): {'char': 'chn', 'type': 'consonant_symbol'},  # upadhmaniya

    # cha
    chr(70677) + chr(70722): {'char': 'cha', 'type': 'consonant_symbol'},  # with virama
    chr(70677) + chr(70723): {'char': 'chan', 'type': 'consonant_symbol'},
    chr(70677) + chr(70724): {'char': 'cham', 'type': 'consonant_symbol'},
    chr(70677) + chr(70725): {'char': 'chah', 'type': 'consonant_symbol'},
    chr(70677) + chr(70726): {'char': 'cha', 'type': 'consonant_symbol'},  # empty symbol
    chr(70677) + chr(70727): {'char': 'cha', 'type': 'consonant_symbol'},  # empty symbol
    chr(70677) + chr(70728): {'char': 'cham', 'type': 'consonant_symbol'},  # final anusvara
    chr(70677) + chr(70729): {'char': 'chaom', 'type': 'consonant_symbol'},
    chr(70677) + chr(70730): {'char': 'chan', 'type': 'consonant_symbol'},  # siddhi
    chr(70677) + chr(70747): {'char': 'cha', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70677) + chr(70748): {'char': 'cha', 'type': 'consonant_symbol'},  # reserved
    chr(70677) + chr(70749): {'char': 'cha', 'type': 'consonant_symbol'},  # insertion sign
    chr(70677) + chr(70750): {'char': 'cha', 'type': 'consonant_symbol'},  # sandhi
    chr(70677) + chr(70751): {'char': 'cham', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70677) + chr(70752): {'char': 'chat', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70677) + chr(70753): {'char': 'chan', 'type': 'consonant_symbol'},  # upadhmaniya

    # j
    chr(70678) + chr(70722): {'char': 'j', 'type': 'consonant_symbol'},  # with virama
    chr(70678) + chr(70723): {'char': 'jn', 'type': 'consonant_symbol'},
    chr(70678) + chr(70724): {'char': 'jm', 'type': 'consonant_symbol'},
    chr(70678) + chr(70725): {'char': 'jh', 'type': 'consonant_symbol'},
    chr(70678) + chr(70726): {'char': 'j', 'type': 'consonant_symbol'},  # empty symbol
    chr(70678) + chr(70727): {'char': 'j', 'type': 'consonant_symbol'},  # empty symbol
    chr(70678) + chr(70728): {'char': 'jm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70678) + chr(70729): {'char': 'jom', 'type': 'consonant_symbol'},
    chr(70678) + chr(70730): {'char': 'jn', 'type': 'consonant_symbol'},  # siddhi
    chr(70678) + chr(70747): {'char': 'j', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70678) + chr(70748): {'char': 'j', 'type': 'consonant_symbol'},  # reserved
    chr(70678) + chr(70749): {'char': 'j', 'type': 'consonant_symbol'},  # insertion sign
    chr(70678) + chr(70750): {'char': 'j', 'type': 'consonant_symbol'},  # sandhi
    chr(70678) + chr(70751): {'char': 'jm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70678) + chr(70752): {'char': 'jt', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70678) + chr(70753): {'char': 'jn', 'type': 'consonant_symbol'},  # upadhmaniya

    # jh
    chr(70679) + chr(70722): {'char': 'jh', 'type': 'consonant_symbol'},  # with virama
    chr(70679) + chr(70723): {'char': 'jhn', 'type': 'consonant_symbol'},
    chr(70679) + chr(70724): {'char': 'jhm', 'type': 'consonant_symbol'},
    chr(70679) + chr(70725): {'char': 'jhh', 'type': 'consonant_symbol'},
    chr(70679) + chr(70726): {'char': 'jh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70679) + chr(70727): {'char': 'jh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70679) + chr(70728): {'char': 'jhm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70679) + chr(70729): {'char': 'jhom', 'type': 'consonant_symbol'},
    chr(70679) + chr(70730): {'char': 'jhn', 'type': 'consonant_symbol'},  # siddhi
    chr(70679) + chr(70747): {'char': 'jh', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70679) + chr(70748): {'char': 'jh', 'type': 'consonant_symbol'},  # reserved
    chr(70679) + chr(70749): {'char': 'jh', 'type': 'consonant_symbol'},  # insertion sign
    chr(70679) + chr(70750): {'char': 'jh', 'type': 'consonant_symbol'},  # sandhi
    chr(70679) + chr(70751): {'char': 'jhm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70679) + chr(70752): {'char': 'jht', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70679) + chr(70753): {'char': 'jhn', 'type': 'consonant_symbol'},  # upadhmaniya

    # ny
    chr(70680) + chr(70722): {'char': 'ny', 'type': 'consonant_symbol'},  # with virama
    chr(70680) + chr(70723): {'char': 'nyn', 'type': 'consonant_symbol'},
    chr(70680) + chr(70724): {'char': 'nym', 'type': 'consonant_symbol'},
    chr(70680) + chr(70725): {'char': 'nyh', 'type': 'consonant_symbol'},
    chr(70680) + chr(70726): {'char': 'ny', 'type': 'consonant_symbol'},  # empty symbol
    chr(70680) + chr(70727): {'char': 'ny', 'type': 'consonant_symbol'},  # empty symbol
    chr(70680) + chr(70728): {'char': 'nym', 'type': 'consonant_symbol'},  # final anusvara
    chr(70680) + chr(70729): {'char': 'nyom', 'type': 'consonant_symbol'},
    chr(70680) + chr(70730): {'char': 'nyn', 'type': 'consonant_symbol'},  # siddhi
    chr(70680) + chr(70747): {'char': 'ny', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70680) + chr(70748): {'char': 'ny', 'type': 'consonant_symbol'},  # reserved
    chr(70680) + chr(70749): {'char': 'ny', 'type': 'consonant_symbol'},  # insertion sign
    chr(70680) + chr(70750): {'char': 'ny', 'type': 'consonant_symbol'},  # sandhi
    chr(70680) + chr(70751): {'char': 'nym', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70680) + chr(70752): {'char': 'nyt', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70680) + chr(70753): {'char': 'nyn', 'type': 'consonant_symbol'},  # upadhmaniya

    # nyh
    chr(70681) + chr(70722): {'char': 'nyh', 'type': 'consonant_symbol'},  # with virama
    chr(70681) + chr(70723): {'char': 'nyhn', 'type': 'consonant_symbol'},
    chr(70681) + chr(70724): {'char': 'nyhm', 'type': 'consonant_symbol'},
    chr(70681) + chr(70725): {'char': 'nyhh', 'type': 'consonant_symbol'},
    chr(70681) + chr(70726): {'char': 'nyh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70681) + chr(70727): {'char': 'nyh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70681) + chr(70728): {'char': 'nyhm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70681) + chr(70729): {'char': 'nyhom', 'type': 'consonant_symbol'},
    chr(70681) + chr(70730): {'char': 'nyhn', 'type': 'consonant_symbol'},  # siddhi
    chr(70681) + chr(70747): {'char': 'nyh', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70681) + chr(70748): {'char': 'nyh', 'type': 'consonant_symbol'},  # reserved
    chr(70681) + chr(70749): {'char': 'nyh', 'type': 'consonant_symbol'},  # insertion sign
    chr(70681) + chr(70750): {'char': 'nyh', 'type': 'consonant_symbol'},  # sandhi
    chr(70681) + chr(70751): {'char': 'nyhm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70681) + chr(70752): {'char': 'nyht', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70681) + chr(70753): {'char': 'nyhn', 'type': 'consonant_symbol'},  # upadhmaniya

    # tt
    chr(70682) + chr(70722): {'char': 'tt', 'type': 'consonant_symbol'},  # with virama
    chr(70682) + chr(70723): {'char': 'ttn', 'type': 'consonant_symbol'},
    chr(70682) + chr(70724): {'char': 'ttm', 'type': 'consonant_symbol'},
    chr(70682) + chr(70725): {'char': 'tth', 'type': 'consonant_symbol'},
    chr(70682) + chr(70726): {'char': 'tt', 'type': 'consonant_symbol'},  # empty symbol
    chr(70682) + chr(70727): {'char': 'tt', 'type': 'consonant_symbol'},  # empty symbol
    chr(70682) + chr(70728): {'char': 'ttm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70682) + chr(70729): {'char': 'ttom', 'type': 'consonant_symbol'},
    chr(70682) + chr(70730): {'char': 'ttn', 'type': 'consonant_symbol'},  # siddhi
    chr(70682) + chr(70747): {'char': 'tt', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70682) + chr(70748): {'char': 'tt', 'type': 'consonant_symbol'},  # reserved
    chr(70682) + chr(70749): {'char': 'tt', 'type': 'consonant_symbol'},  # insertion sign
    chr(70682) + chr(70750): {'char': 'tt', 'type': 'consonant_symbol'},  # sandhi
    chr(70682) + chr(70751): {'char': 'ttm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70682) + chr(70752): {'char': 'ttt', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70682) + chr(70753): {'char': 'ttn', 'type': 'consonant_symbol'},  # upadhmaniya

    # tth
    chr(70683) + chr(70722): {'char': 'tth', 'type': 'consonant_symbol'},  # with virama
    chr(70683) + chr(70723): {'char': 'tthn', 'type': 'consonant_symbol'},
    chr(70683) + chr(70724): {'char': 'tthm', 'type': 'consonant_symbol'},
    chr(70683) + chr(70725): {'char': 'tthh', 'type': 'consonant_symbol'},
    chr(70683) + chr(70726): {'char': 'tth', 'type': 'consonant_symbol'},  # empty symbol
    chr(70683) + chr(70727): {'char': 'tth', 'type': 'consonant_symbol'},  # empty symbol
    chr(70683) + chr(70728): {'char': 'tthm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70683) + chr(70729): {'char': 'tthom', 'type': 'consonant_symbol'},
    chr(70683) + chr(70730): {'char': 'tthn', 'type': 'consonant_symbol'},  # siddhi
    chr(70683) + chr(70747): {'char': 'tth', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70683) + chr(70748): {'char': 'tth', 'type': 'consonant_symbol'},  # reserved
    chr(70683) + chr(70749): {'char': 'tth', 'type': 'consonant_symbol'},  # insertion sign
    chr(70683) + chr(70750): {'char': 'tth', 'type': 'consonant_symbol'},  # sandhi
    chr(70683) + chr(70751): {'char': 'tthm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70683) + chr(70752): {'char': 'ttht', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70683) + chr(70753): {'char': 'tthn', 'type': 'consonant_symbol'},  # upadhmaniya

    # dd
    chr(70684) + chr(70722): {'char': 'dd', 'type': 'consonant_symbol'},  # with virama
    chr(70684) + chr(70723): {'char': 'ddn', 'type': 'consonant_symbol'},
    chr(70684) + chr(70724): {'char': 'ddm', 'type': 'consonant_symbol'},
    chr(70684) + chr(70725): {'char': 'ddh', 'type': 'consonant_symbol'},
    chr(70684) + chr(70726): {'char': 'dd', 'type': 'consonant_symbol'},  # empty symbol
    chr(70684) + chr(70727): {'char': 'dd', 'type': 'consonant_symbol'},  # empty symbol
    chr(70684) + chr(70728): {'char': 'ddm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70684) + chr(70729): {'char': 'ddom', 'type': 'consonant_symbol'},
    chr(70684) + chr(70730): {'char': 'ddn', 'type': 'consonant_symbol'},  # siddhi
    chr(70684) + chr(70747): {'char': 'dd', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70684) + chr(70748): {'char': 'dd', 'type': 'consonant_symbol'},  # reserved
    chr(70684) + chr(70749): {'char': 'dd', 'type': 'consonant_symbol'},  # insertion sign
    chr(70684) + chr(70750): {'char': 'dd', 'type': 'consonant_symbol'},  # sandhi
    chr(70684) + chr(70751): {'char': 'ddm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70684) + chr(70752): {'char': 'ddd', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70684) + chr(70753): {'char': 'ddn', 'type': 'consonant_symbol'},  # upadhmaniya

    # ddh
    chr(70685) + chr(70722): {'char': 'ddh', 'type': 'consonant_symbol'},  # with virama
    chr(70685) + chr(70723): {'char': 'ddhn', 'type': 'consonant_symbol'},
    chr(70685) + chr(70724): {'char': 'ddhm', 'type': 'consonant_symbol'},
    chr(70685) + chr(70725): {'char': 'ddhh', 'type': 'consonant_symbol'},
    chr(70685) + chr(70726): {'char': 'ddh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70685) + chr(70727): {'char': 'ddh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70685) + chr(70728): {'char': 'ddhm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70685) + chr(70729): {'char': 'ddhom', 'type': 'consonant_symbol'},
    chr(70685) + chr(70730): {'char': 'ddhn', 'type': 'consonant_symbol'},  # siddhi
    chr(70685) + chr(70747): {'char': 'ddh', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70685) + chr(70748): {'char': 'ddh', 'type': 'consonant_symbol'},  # reserved
    chr(70685) + chr(70749): {'char': 'ddh', 'type': 'consonant_symbol'},  # insertion sign
    chr(70685) + chr(70750): {'char': 'ddh', 'type': 'consonant_symbol'},  # sandhi
    chr(70685) + chr(70751): {'char': 'ddhm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70685) + chr(70752): {'char': 'ddhh', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70685) + chr(70753): {'char': 'ddhn', 'type': 'consonant_symbol'},  # upadhmaniya

    # nn
    chr(70686) + chr(70722): {'char': 'nn', 'type': 'consonant_symbol'},  # with virama
    chr(70686) + chr(70723): {'char': 'nnn', 'type': 'consonant_symbol'},
    chr(70686) + chr(70724): {'char': 'nnm', 'type': 'consonant_symbol'},
    chr(70686) + chr(70725): {'char': 'nnh', 'type': 'consonant_symbol'},
    chr(70686) + chr(70726): {'char': 'nn', 'type': 'consonant_symbol'},  # empty symbol
    chr(70686) + chr(70727): {'char': 'nn', 'type': 'consonant_symbol'},  # empty symbol
    chr(70686) + chr(70728): {'char': 'nnm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70686) + chr(70729): {'char': 'nnom', 'type': 'consonant_symbol'},
    chr(70686) + chr(70730): {'char': 'nnn', 'type': 'consonant_symbol'},  # siddhi
    chr(70686) + chr(70747): {'char': 'nn', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70686) + chr(70748): {'char': 'nn', 'type': 'consonant_symbol'},  # reserved
    chr(70686) + chr(70749): {'char': 'nn', 'type': 'consonant_symbol'},  # insertion sign
    chr(70686) + chr(70750): {'char': 'nn', 'type': 'consonant_symbol'},  # sandhi
    chr(70686) + chr(70751): {'char': 'nnm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70686) + chr(70752): {'char': 'nnn', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70686) + chr(70753): {'char': 'nnn', 'type': 'consonant_symbol'},  # upadhmaniya

    # t
    chr(70687) + chr(70722): {'char': 't', 'type': 'consonant_symbol'},  # with virama
    chr(70687) + chr(70723): {'char': 'tn', 'type': 'consonant_symbol'},
    chr(70687) + chr(70724): {'char': 'tm', 'type': 'consonant_symbol'},
    chr(70687) + chr(70725): {'char': 'th', 'type': 'consonant_symbol'},
    chr(70687) + chr(70726): {'char': 't', 'type': 'consonant_symbol'},  # empty symbol
    chr(70687) + chr(70727): {'char': 't', 'type': 'consonant_symbol'},  # empty symbol
    chr(70687) + chr(70728): {'char': 'tm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70687) + chr(70729): {'char': 'tom', 'type': 'consonant_symbol'},
    chr(70687) + chr(70730): {'char': 'tn', 'type': 'consonant_symbol'},  # siddhi
    chr(70687) + chr(70747): {'char': 't', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70687) + chr(70748): {'char': 't', 'type': 'consonant_symbol'},  # reserved
    chr(70687) + chr(70749): {'char': 't', 'type': 'consonant_symbol'},  # insertion sign
    chr(70687) + chr(70750): {'char': 't', 'type': 'consonant_symbol'},  # sandhi
    chr(70687) + chr(70751): {'char': 'tm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70687) + chr(70752): {'char': 'tt', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70687) + chr(70753): {'char': 'tn', 'type': 'consonant_symbol'},  # upadhmaniya

    # th
    chr(70688) + chr(70722): {'char': 'th', 'type': 'consonant_symbol'},  # with virama
    chr(70688) + chr(70723): {'char': 'thn', 'type': 'consonant_symbol'},
    chr(70688) + chr(70724): {'char': 'thm', 'type': 'consonant_symbol'},
    chr(70688) + chr(70725): {'char': 'thh', 'type': 'consonant_symbol'},
    chr(70688) + chr(70726): {'char': 'th', 'type': 'consonant_symbol'},  # empty symbol
    chr(70688) + chr(70727): {'char': 'th', 'type': 'consonant_symbol'},  # empty symbol
    chr(70688) + chr(70728): {'char': 'thm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70688) + chr(70729): {'char': 'thom', 'type': 'consonant_symbol'},
    chr(70688) + chr(70730): {'char': 'thn', 'type': 'consonant_symbol'},  # siddhi
    chr(70688) + chr(70747): {'char': 'th', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70688) + chr(70748): {'char': 'th', 'type': 'consonant_symbol'},  # reserved
    chr(70688) + chr(70749): {'char': 'th', 'type': 'consonant_symbol'},  # insertion sign
    chr(70688) + chr(70750): {'char': 'th', 'type': 'consonant_symbol'},  # sandhi
    chr(70688) + chr(70751): {'char': 'thm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70688) + chr(70752): {'char': 'thh', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70688) + chr(70753): {'char': 'thn', 'type': 'consonant_symbol'},  # upadhmaniya

    # d
    chr(70689) + chr(70722): {'char': 'd', 'type': 'consonant_symbol'},  # with virama
    chr(70689) + chr(70723): {'char': 'dn', 'type': 'consonant_symbol'},
    chr(70689) + chr(70724): {'char': 'dm', 'type': 'consonant_symbol'},
    chr(70689) + chr(70725): {'char': 'dh', 'type': 'consonant_symbol'},
    chr(70689) + chr(70726): {'char': 'd', 'type': 'consonant_symbol'},  # empty symbol
    chr(70689) + chr(70727): {'char': 'd', 'type': 'consonant_symbol'},  # empty symbol
    chr(70689) + chr(70728): {'char': 'dm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70689) + chr(70729): {'char': 'dom', 'type': 'consonant_symbol'},
    chr(70689) + chr(70730): {'char': 'dn', 'type': 'consonant_symbol'},  # siddhi
    chr(70689) + chr(70747): {'char': 'd', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70689) + chr(70748): {'char': 'd', 'type': 'consonant_symbol'},  # reserved
    chr(70689) + chr(70749): {'char': 'd', 'type': 'consonant_symbol'},  # insertion sign
    chr(70689) + chr(70750): {'char': 'd', 'type': 'consonant_symbol'},  # sandhi
    chr(70689) + chr(70751): {'char': 'dm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70689) + chr(70752): {'char': 'dd', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70689) + chr(70753): {'char': 'dn', 'type': 'consonant_symbol'},  # upadhmaniya

    # dh
    chr(70690) + chr(70722): {'char': 'dh', 'type': 'consonant_symbol'},  # with virama
    chr(70690) + chr(70723): {'char': 'dhn', 'type': 'consonant_symbol'},
    chr(70690) + chr(70724): {'char': 'dhm', 'type': 'consonant_symbol'},
    chr(70690) + chr(70725): {'char': 'dhh', 'type': 'consonant_symbol'},
    chr(70690) + chr(70726): {'char': 'dh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70690) + chr(70727): {'char': 'dh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70690) + chr(70728): {'char': 'dhm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70690) + chr(70729): {'char': 'dhom', 'type': 'consonant_symbol'},
    chr(70690) + chr(70730): {'char': 'dhn', 'type': 'consonant_symbol'},  # siddhi
    chr(70690) + chr(70747): {'char': 'dh', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70690) + chr(70748): {'char': 'dh', 'type': 'consonant_symbol'},  # reserved
    chr(70690) + chr(70749): {'char': 'dh', 'type': 'consonant_symbol'},  # insertion sign
    chr(70690) + chr(70750): {'char': 'dh', 'type': 'consonant_symbol'},  # sandhi
    chr(70690) + chr(70751): {'char': 'dhm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70690) + chr(70752): {'char': 'dhh', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70690) + chr(70753): {'char': 'dhn', 'type': 'consonant_symbol'},  # upadhmaniya

    # n
    chr(70691) + chr(70722): {'char': 'n', 'type': 'consonant_symbol'},  # with virama
    chr(70691) + chr(70723): {'char': 'nn', 'type': 'consonant_symbol'},
    chr(70691) + chr(70724): {'char': 'nm', 'type': 'consonant_symbol'},
    chr(70691) + chr(70725): {'char': 'nh', 'type': 'consonant_symbol'},
    chr(70691) + chr(70726): {'char': 'n', 'type': 'consonant_symbol'},  # empty symbol
    chr(70691) + chr(70727): {'char': 'n', 'type': 'consonant_symbol'},  # empty symbol
    chr(70691) + chr(70728): {'char': 'nm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70691) + chr(70729): {'char': 'nom', 'type': 'consonant_symbol'},
    chr(70691) + chr(70730): {'char': 'nn', 'type': 'consonant_symbol'},  # siddhi
    chr(70691) + chr(70747): {'char': 'n', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70691) + chr(70748): {'char': 'n', 'type': 'consonant_symbol'},  # reserved
    chr(70691) + chr(70749): {'char': 'n', 'type': 'consonant_symbol'},  # insertion sign
    chr(70691) + chr(70750): {'char': 'n', 'type': 'consonant_symbol'},  # sandhi
    chr(70691) + chr(70751): {'char': 'nm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70691) + chr(70752): {'char': 'nn', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70691) + chr(70753): {'char': 'nn', 'type': 'consonant_symbol'},  # upadhmaniya

    # nh
    chr(70692) + chr(70722): {'char': 'nh', 'type': 'consonant_symbol'},  # with virama
    chr(70692) + chr(70723): {'char': 'nhn', 'type': 'consonant_symbol'},
    chr(70692) + chr(70724): {'char': 'nhm', 'type': 'consonant_symbol'},
    chr(70692) + chr(70725): {'char': 'nhh', 'type': 'consonant_symbol'},
    chr(70692) + chr(70726): {'char': 'nh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70692) + chr(70727): {'char': 'nh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70692) + chr(70728): {'char': 'nhm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70692) + chr(70729): {'char': 'nhom', 'type': 'consonant_symbol'},
    chr(70692) + chr(70730): {'char': 'nhn', 'type': 'consonant_symbol'},  # siddhi
    chr(70692) + chr(70747): {'char': 'nh', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70692) + chr(70748): {'char': 'nh', 'type': 'consonant_symbol'},  # reserved
    chr(70692) + chr(70749): {'char': 'nh', 'type': 'consonant_symbol'},  # insertion sign
    chr(70692) + chr(70750): {'char': 'nh', 'type': 'consonant_symbol'},  # sandhi
    chr(70692) + chr(70751): {'char': 'nhm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70692) + chr(70752): {'char': 'nhh', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70692) + chr(70753): {'char': 'nhn', 'type': 'consonant_symbol'},  # upadhmaniya

    # p
    chr(70693) + chr(70722): {'char': 'p', 'type': 'consonant_symbol'},  # with virama
    chr(70693) + chr(70723): {'char': 'pn', 'type': 'consonant_symbol'},
    chr(70693) + chr(70724): {'char': 'pm', 'type': 'consonant_symbol'},
    chr(70693) + chr(70725): {'char': 'ph', 'type': 'consonant_symbol'},
    chr(70693) + chr(70726): {'char': 'p', 'type': 'consonant_symbol'},  # empty symbol
    chr(70693) + chr(70727): {'char': 'p', 'type': 'consonant_symbol'},  # empty symbol
    chr(70693) + chr(70728): {'char': 'pm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70693) + chr(70729): {'char': 'pom', 'type': 'consonant_symbol'},
    chr(70693) + chr(70730): {'char': 'pn', 'type': 'consonant_symbol'},  # siddhi
    chr(70693) + chr(70747): {'char': 'p', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70693) + chr(70748): {'char': 'p', 'type': 'consonant_symbol'},  # reserved
    chr(70693) + chr(70749): {'char': 'p', 'type': 'consonant_symbol'},  # insertion sign
    chr(70693) + chr(70750): {'char': 'p', 'type': 'consonant_symbol'},  # sandhi
    chr(70693) + chr(70751): {'char': 'pm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70693) + chr(70752): {'char': 'pp', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70693) + chr(70753): {'char': 'pn', 'type': 'consonant_symbol'},  # upadhmaniya

    # ph
    chr(70694) + chr(70722): {'char': 'ph', 'type': 'consonant_symbol'},  # with virama
    chr(70694) + chr(70723): {'char': 'phn', 'type': 'consonant_symbol'},
    chr(70694) + chr(70724): {'char': 'phm', 'type': 'consonant_symbol'},
    chr(70694) + chr(70725): {'char': 'phh', 'type': 'consonant_symbol'},
    chr(70694) + chr(70726): {'char': 'ph', 'type': 'consonant_symbol'},  # empty symbol
    chr(70694) + chr(70727): {'char': 'ph', 'type': 'consonant_symbol'},  # empty symbol
    chr(70694) + chr(70728): {'char': 'phm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70694) + chr(70729): {'char': 'phom', 'type': 'consonant_symbol'},
    chr(70694) + chr(70730): {'char': 'phn', 'type': 'consonant_symbol'},  # siddhi
    chr(70694) + chr(70747): {'char': 'ph', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70694) + chr(70748): {'char': 'ph', 'type': 'consonant_symbol'},  # reserved
    chr(70694) + chr(70749): {'char': 'ph', 'type': 'consonant_symbol'},  # insertion sign
    chr(70694) + chr(70750): {'char': 'ph', 'type': 'consonant_symbol'},  # sandhi
    chr(70694) + chr(70751): {'char': 'phm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70694) + chr(70752): {'char': 'phh', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70694) + chr(70753): {'char': 'phn', 'type': 'consonant_symbol'},  # upadhmaniya

    # b
    chr(70695) + chr(70722): {'char': 'b', 'type': 'consonant_symbol'},  # with virama
    chr(70695) + chr(70723): {'char': 'bn', 'type': 'consonant_symbol'},
    chr(70695) + chr(70724): {'char': 'bm', 'type': 'consonant_symbol'},
    chr(70695) + chr(70725): {'char': 'bh', 'type': 'consonant_symbol'},
    chr(70695) + chr(70726): {'char': 'b', 'type': 'consonant_symbol'},  # empty symbol
    chr(70695) + chr(70727): {'char': 'b', 'type': 'consonant_symbol'},  # empty symbol
    chr(70695) + chr(70728): {'char': 'bm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70695) + chr(70729): {'char': 'bom', 'type': 'consonant_symbol'},
    chr(70695) + chr(70730): {'char': 'bn', 'type': 'consonant_symbol'},  # siddhi
    chr(70695) + chr(70747): {'char': 'b', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70695) + chr(70748): {'char': 'b', 'type': 'consonant_symbol'},  # reserved
    chr(70695) + chr(70749): {'char': 'b', 'type': 'consonant_symbol'},  # insertion sign
    chr(70695) + chr(70750): {'char': 'b', 'type': 'consonant_symbol'},  # sandhi
    chr(70695) + chr(70751): {'char': 'bm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70695) + chr(70752): {'char': 'bb', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70695) + chr(70753): {'char': 'bn', 'type': 'consonant_symbol'},  # upadhmaniya

    # bh
    chr(70696) + chr(70722): {'char': 'bh', 'type': 'consonant_symbol'},  # with virama
    chr(70696) + chr(70723): {'char': 'bhn', 'type': 'consonant_symbol'},
    chr(70696) + chr(70724): {'char': 'bhm', 'type': 'consonant_symbol'},
    chr(70696) + chr(70725): {'char': 'bhh', 'type': 'consonant_symbol'},
    chr(70696) + chr(70726): {'char': 'bh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70696) + chr(70727): {'char': 'bh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70696) + chr(70728): {'char': 'bhm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70696) + chr(70729): {'char': 'bhom', 'type': 'consonant_symbol'},
    chr(70696) + chr(70730): {'char': 'bhn', 'type': 'consonant_symbol'},  # siddhi
    chr(70696) + chr(70747): {'char': 'bh', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70696) + chr(70748): {'char': 'bh', 'type': 'consonant_symbol'},  # reserved
    chr(70696) + chr(70749): {'char': 'bh', 'type': 'consonant_symbol'},  # insertion sign
    chr(70696) + chr(70750): {'char': 'bh', 'type': 'consonant_symbol'},  # sandhi
    chr(70696) + chr(70751): {'char': 'bhm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70696) + chr(70752): {'char': 'bhh', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70696) + chr(70753): {'char': 'bhn', 'type': 'consonant_symbol'},  # upadhmaniya

    # m
    chr(70697) + chr(70722): {'char': 'm', 'type': 'consonant_symbol'},  # with virama
    chr(70697) + chr(70723): {'char': 'mn', 'type': 'consonant_symbol'},
    chr(70697) + chr(70724): {'char': 'mm', 'type': 'consonant_symbol'},
    chr(70697) + chr(70725): {'char': 'mh', 'type': 'consonant_symbol'},
    chr(70697) + chr(70726): {'char': 'm', 'type': 'consonant_symbol'},  # empty symbol
    chr(70697) + chr(70727): {'char': 'm', 'type': 'consonant_symbol'},  # empty symbol
    chr(70697) + chr(70728): {'char': 'mm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70697) + chr(70729): {'char': 'mom', 'type': 'consonant_symbol'},
    chr(70697) + chr(70730): {'char': 'mn', 'type': 'consonant_symbol'},  # siddhi
    chr(70697) + chr(70747): {'char': 'm', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70697) + chr(70748): {'char': 'm', 'type': 'consonant_symbol'},  # reserved
    chr(70697) + chr(70749): {'char': 'm', 'type': 'consonant_symbol'},  # insertion sign
    chr(70697) + chr(70750): {'char': 'm', 'type': 'consonant_symbol'},  # sandhi
    chr(70697) + chr(70751): {'char': 'mm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70697) + chr(70752): {'char': 'mm', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70697) + chr(70753): {'char': 'mn', 'type': 'consonant_symbol'},  # upadhmaniya

    # mh
    chr(70698) + chr(70722): {'char': 'mh', 'type': 'consonant_symbol'},  # with virama
    chr(70698) + chr(70723): {'char': 'mhn', 'type': 'consonant_symbol'},
    chr(70698) + chr(70724): {'char': 'mh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70698) + chr(70725): {'char': 'mh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70698) + chr(70728): {'char': 'mh', 'type': 'consonant_symbol'},  # final anusvara
    chr(70698) + chr(70729): {'char': 'mhom', 'type': 'consonant_symbol'},
    chr(70698) + chr(70730): {'char': 'mhn', 'type': 'consonant_symbol'},  # siddhi
    chr(70698) + chr(70747): {'char': 'mh', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70698) + chr(70748): {'char': 'mh', 'type': 'consonant_symbol'},  # reserved
    chr(70698) + chr(70749): {'char': 'mh', 'type': 'consonant_symbol'},  # insertion sign
    chr(70698) + chr(70750): {'char': 'mh', 'type': 'consonant_symbol'},  # sandhi
    chr(70698) + chr(70751): {'char': 'mh', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70698) + chr(70752): {'char': 'mh', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70698) + chr(70753): {'char': 'mhn', 'type': 'consonant_symbol'},  # upadhmaniya

    # y
    chr(70699) + chr(70722): {'char': 'y', 'type': 'consonant_symbol'},  # with virama
    chr(70699) + chr(70723): {'char': 'yn', 'type': 'consonant_symbol'},
    chr(70699) + chr(70724): {'char': 'ym', 'type': 'consonant_symbol'},
    chr(70699) + chr(70725): {'char': 'yh', 'type': 'consonant_symbol'},
    chr(70699) + chr(70726): {'char': 'y', 'type': 'consonant_symbol'},  # empty symbol
    chr(70699) + chr(70727): {'char': 'y', 'type': 'consonant_symbol'},  # empty symbol
    chr(70699) + chr(70728): {'char': 'ym', 'type': 'consonant_symbol'},  # final anusvara
    chr(70699) + chr(70729): {'char': 'yom', 'type': 'consonant_symbol'},
    chr(70699) + chr(70730): {'char': 'yn', 'type': 'consonant_symbol'},  # siddhi
    chr(70699) + chr(70747): {'char': 'y', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70699) + chr(70748): {'char': 'y', 'type': 'consonant_symbol'},  # reserved
    chr(70699) + chr(70749): {'char': 'y', 'type': 'consonant_symbol'},  # insertion sign
    chr(70699) + chr(70750): {'char': 'y', 'type': 'consonant_symbol'},  # sandhi
    chr(70699) + chr(70751): {'char': 'ym', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70699) + chr(70752): {'char': 'yy', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70699) + chr(70753): {'char': 'yn', 'type': 'consonant_symbol'},  # upadhmaniya

    # r
    chr(70700) + chr(70722): {'char': 'r', 'type': 'consonant_symbol'},  # with virama
    chr(70700) + chr(70723): {'char': 'rn', 'type': 'consonant_symbol'},
    chr(70700) + chr(70724): {'char': 'rm', 'type': 'consonant_symbol'},
    chr(70700) + chr(70725): {'char': 'rh', 'type': 'consonant_symbol'},
    chr(70700) + chr(70726): {'char': 'r', 'type': 'consonant_symbol'},  # empty symbol
    chr(70700) + chr(70727): {'char': 'r', 'type': 'consonant_symbol'},  # empty symbol
    chr(70700) + chr(70728): {'char': 'rm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70700) + chr(70729): {'char': 'rom', 'type': 'consonant_symbol'},
    chr(70700) + chr(70730): {'char': 'rn', 'type': 'consonant_symbol'},  # siddhi
    chr(70700) + chr(70747): {'char': 'r', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70700) + chr(70748): {'char': 'r', 'type': 'consonant_symbol'},  # reserved
    chr(70700) + chr(70749): {'char': 'r', 'type': 'consonant_symbol'},  # insertion sign
    chr(70700) + chr(70750): {'char': 'r', 'type': 'consonant_symbol'},  # sandhi
    chr(70700) + chr(70751): {'char': 'rm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70700) + chr(70752): {'char': 'rr', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70700) + chr(70753): {'char': 'rn', 'type': 'consonant_symbol'},  # upadhmaniya

    # rh
    chr(70701) + chr(70722): {'char': 'rh', 'type': 'consonant_symbol'},  # with virama
    chr(70701) + chr(70723): {'char': 'rhn', 'type': 'consonant_symbol'},
    chr(70701) + chr(70724): {'char': 'rhm', 'type': 'consonant_symbol'},
    chr(70701) + chr(70725): {'char': 'rhh', 'type': 'consonant_symbol'},
    chr(70701) + chr(70726): {'char': 'rh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70701) + chr(70727): {'char': 'rh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70701) + chr(70728): {'char': 'rhm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70701) + chr(70729): {'char': 'rhom', 'type': 'consonant_symbol'},
    chr(70701) + chr(70730): {'char': 'rhn', 'type': 'consonant_symbol'},  # siddhi
    chr(70701) + chr(70747): {'char': 'rh', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70701) + chr(70748): {'char': 'rh', 'type': 'consonant_symbol'},  # reserved
    chr(70701) + chr(70749): {'char': 'rh', 'type': 'consonant_symbol'},  # insertion sign
    chr(70701) + chr(70750): {'char': 'rh', 'type': 'consonant_symbol'},  # sandhi
    chr(70701) + chr(70751): {'char': 'rhm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70701) + chr(70752): {'char': 'rhh', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70701) + chr(70753): {'char': 'rhn', 'type': 'consonant_symbol'},  # upadhmaniya

    # l
    chr(70702) + chr(70722): {'char': 'l', 'type': 'consonant_symbol'},  # with virama
    chr(70702) + chr(70723): {'char': 'ln', 'type': 'consonant_symbol'},
    chr(70702) + chr(70724): {'char': 'lm', 'type': 'consonant_symbol'},
    chr(70702) + chr(70725): {'char': 'lh', 'type': 'consonant_symbol'},
    chr(70702) + chr(70726): {'char': 'l', 'type': 'consonant_symbol'},  # empty symbol
    chr(70702) + chr(70727): {'char': 'l', 'type': 'consonant_symbol'},  # empty symbol
    chr(70702) + chr(70728): {'char': 'lm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70702) + chr(70729): {'char': 'lom', 'type': 'consonant_symbol'},
    chr(70702) + chr(70730): {'char': 'ln', 'type': 'consonant_symbol'},  # siddhi
    chr(70702) + chr(70747): {'char': 'l', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70702) + chr(70748): {'char': 'l', 'type': 'consonant_symbol'},  # reserved
    chr(70702) + chr(70749): {'char': 'l', 'type': 'consonant_symbol'},  # insertion sign
    chr(70702) + chr(70750): {'char': 'l', 'type': 'consonant_symbol'},  # sandhi
    chr(70702) + chr(70751): {'char': 'lm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70702) + chr(70752): {'char': 'll', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70702) + chr(70753): {'char': 'ln', 'type': 'consonant_symbol'},  # upadhmaniya

    # lh
    chr(70703) + chr(70722): {'char': 'lh', 'type': 'consonant_symbol'},  # with virama
    chr(70703) + chr(70723): {'char': 'lhn', 'type': 'consonant_symbol'},
    chr(70703) + chr(70724): {'char': 'lhm', 'type': 'consonant_symbol'},
    chr(70703) + chr(70725): {'char': 'lhh', 'type': 'consonant_symbol'},
    chr(70703) + chr(70726): {'char': 'lh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70703) + chr(70727): {'char': 'lh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70703) + chr(70728): {'char': 'lhm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70703) + chr(70729): {'char': 'lhom', 'type': 'consonant_symbol'},
    chr(70703) + chr(70730): {'char': 'lhn', 'type': 'consonant_symbol'},  # siddhi
    chr(70703) + chr(70747): {'char': 'lh', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70703) + chr(70748): {'char': 'lh', 'type': 'consonant_symbol'},  # reserved
    chr(70703) + chr(70749): {'char': 'lh', 'type': 'consonant_symbol'},  # insertion sign
    chr(70703) + chr(70750): {'char': 'lh', 'type': 'consonant_symbol'},  # sandhi
    chr(70703) + chr(70751): {'char': 'lhm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70703) + chr(70752): {'char': 'lhh', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70703) + chr(70753): {'char': 'lhn', 'type': 'consonant_symbol'},  # upadhmaniya

    # w
    chr(70704) + chr(70722): {'char': 'w', 'type': 'consonant_symbol'},  # with virama
    chr(70704) + chr(70723): {'char': 'wn', 'type': 'consonant_symbol'},
    chr(70704) + chr(70724): {'char': 'wm', 'type': 'consonant_symbol'},
    chr(70704) + chr(70725): {'char': 'wh', 'type': 'consonant_symbol'},
    chr(70704) + chr(70726): {'char': 'w', 'type': 'consonant_symbol'},  # empty symbol
    chr(70704) + chr(70727): {'char': 'w', 'type': 'consonant_symbol'},  # empty symbol
    chr(70704) + chr(70728): {'char': 'wm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70704) + chr(70729): {'char': 'wom', 'type': 'consonant_symbol'},
    chr(70704) + chr(70730): {'char': 'wn', 'type': 'consonant_symbol'},  # siddhi
    chr(70704) + chr(70747): {'char': 'w', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70704) + chr(70748): {'char': 'w', 'type': 'consonant_symbol'},  # reserved
    chr(70704) + chr(70749): {'char': 'w', 'type': 'consonant_symbol'},  # insertion sign
    chr(70704) + chr(70750): {'char': 'w', 'type': 'consonant_symbol'},  # sandhi
    chr(70704) + chr(70751): {'char': 'wm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70704) + chr(70752): {'char': 'ww', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70704) + chr(70753): {'char': 'wn', 'type': 'consonant_symbol'},  # upadhmaniya

    # sh
    chr(70705) + chr(70722): {'char': 'sh', 'type': 'consonant_symbol'},  # with virama
    chr(70705) + chr(70723): {'char': 'shn', 'type': 'consonant_symbol'},
    chr(70705) + chr(70724): {'char': 'shm', 'type': 'consonant_symbol'},
    chr(70705) + chr(70725): {'char': 'shh', 'type': 'consonant_symbol'},
    chr(70705) + chr(70726): {'char': 'sh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70705) + chr(70727): {'char': 'sh', 'type': 'consonant_symbol'},  # empty symbol
    chr(70705) + chr(70728): {'char': 'shm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70705) + chr(70729): {'char': 'shom', 'type': 'consonant_symbol'},
    chr(70705) + chr(70730): {'char': 'shn', 'type': 'consonant_symbol'},  # siddhi
    chr(70705) + chr(70747): {'char': 'sh', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70705) + chr(70748): {'char': 'sh', 'type': 'consonant_symbol'},  # reserved
    chr(70705) + chr(70749): {'char': 'sh', 'type': 'consonant_symbol'},  # insertion sign
    chr(70705) + chr(70750): {'char': 'sh', 'type': 'consonant_symbol'},  # sandhi
    chr(70705) + chr(70751): {'char': 'shm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70705) + chr(70752): {'char': 'shh', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70705) + chr(70753): {'char': 'shn', 'type': 'consonant_symbol'},  # upadhmaniya

    # ss
    chr(70706) + chr(70722): {'char': 'ss', 'type': 'consonant_symbol'},  # with virama
    chr(70706) + chr(70723): {'char': 'ssn', 'type': 'consonant_symbol'},
    chr(70706) + chr(70724): {'char': 'ssm', 'type': 'consonant_symbol'},
    chr(70706) + chr(70725): {'char': 'ssh', 'type': 'consonant_symbol'},
    chr(70706) + chr(70726): {'char': 'ss', 'type': 'consonant_symbol'},  # empty symbol
    chr(70706) + chr(70727): {'char': 'ss', 'type': 'consonant_symbol'},  # empty symbol
    chr(70706) + chr(70728): {'char': 'ssm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70706) + chr(70729): {'char': 'ssom', 'type': 'consonant_symbol'},
    chr(70706) + chr(70730): {'char': 'ssn', 'type': 'consonant_symbol'},  # siddhi
    chr(70706) + chr(70747): {'char': 'ss', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70706) + chr(70748): {'char': 'ss', 'type': 'consonant_symbol'},  # reserved
    chr(70706) + chr(70749): {'char': 'ss', 'type': 'consonant_symbol'},  # insertion sign
    chr(70706) + chr(70750): {'char': 'ss', 'type': 'consonant_symbol'},  # sandhi
    chr(70706) + chr(70751): {'char': 'ssm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70706) + chr(70752): {'char': 'sss', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70706) + chr(70753): {'char': 'ssn', 'type': 'consonant_symbol'},  # upadhmaniya

    # s
    chr(70707) + chr(70722): {'char': 's', 'type': 'consonant_symbol'},  # with virama
    chr(70707) + chr(70723): {'char': 'sn', 'type': 'consonant_symbol'},
    chr(70707) + chr(70724): {'char': 'sm', 'type': 'consonant_symbol'},
    chr(70707) + chr(70725): {'char': 'sh', 'type': 'consonant_symbol'},
    chr(70707) + chr(70726): {'char': 's', 'type': 'consonant_symbol'},  # empty symbol
    chr(70707) + chr(70727): {'char': 's', 'type': 'consonant_symbol'},  # empty symbol
    chr(70707) + chr(70728): {'char': 'sm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70707) + chr(70729): {'char': 'som', 'type': 'consonant_symbol'},
    chr(70707) + chr(70730): {'char': 'sn', 'type': 'consonant_symbol'},  # siddhi
    chr(70707) + chr(70747): {'char': 's', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70707) + chr(70748): {'char': 's', 'type': 'consonant_symbol'},  # reserved
    chr(70707) + chr(70749): {'char': 's', 'type': 'consonant_symbol'},  # insertion sign
    chr(70707) + chr(70750): {'char': 's', 'type': 'consonant_symbol'},  # sandhi
    chr(70707) + chr(70751): {'char': 'sm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70707) + chr(70752): {'char': 'ss', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70707) + chr(70753): {'char': 'sn', 'type': 'consonant_symbol'},  # upadhmaniya

    # h
    chr(70708) + chr(70722): {'char': 'h', 'type': 'consonant_symbol'},  # with virama
    chr(70708) + chr(70723): {'char': 'hn', 'type': 'consonant_symbol'},
    chr(70708) + chr(70724): {'char': 'hm', 'type': 'consonant_symbol'},
    chr(70708) + chr(70725): {'char': 'hh', 'type': 'consonant_symbol'},
    chr(70708) + chr(70726): {'char': 'h', 'type': 'consonant_symbol'},  # empty symbol
    chr(70708) + chr(70727): {'char': 'h', 'type': 'consonant_symbol'},  # empty symbol
    chr(70708) + chr(70728): {'char': 'hm', 'type': 'consonant_symbol'},  # final anusvara
    chr(70708) + chr(70729): {'char': 'hom', 'type': 'consonant_symbol'},
    chr(70708) + chr(70730): {'char': 'hn', 'type': 'consonant_symbol'},  # siddhi
    chr(70708) + chr(70747): {'char': 'h', 'type': 'consonant_symbol'},  # placeholder mark
    chr(70708) + chr(70748): {'char': 'h', 'type': 'consonant_symbol'},  # reserved
    chr(70708) + chr(70749): {'char': 'h', 'type': 'consonant_symbol'},  # insertion sign
    chr(70708) + chr(70750): {'char': 'h', 'type': 'consonant_symbol'},  # sandhi
    chr(70708) + chr(70751): {'char': 'hm', 'type': 'consonant_symbol'},  # vedic anusarva
    chr(70708) + chr(70752): {'char': 'hh', 'type': 'consonant_symbol'},  # jihvamuliya
    chr(70708) + chr(70753): {'char': 'hn', 'type': 'consonant_symbol'},  # upadhmaniya

    # Consonants followed by punctuation

    # k
    chr(70670) + chr(70731): {'char': 'k.', 'type': 'consonant_punctuation'},
    chr(70670) + chr(70732): {'char': 'k.', 'type': 'consonant_punctuation'},
    chr(70670) + chr(70733): {'char': 'k,', 'type': 'consonant_punctuation'},
    chr(70670) + chr(70734): {'char': 'k..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70670) + chr(70735): {'char': 'k...', 'type': 'consonant_punctuation'},
    chr(70670) + chr(70746): {'char': 'k', 'type': 'consonant_punctuation'},  # double comma

    # kh
    chr(70671) + chr(70731): {'char': 'kh.', 'type': 'consonant_punctuation'},
    chr(70671) + chr(70732): {'char': 'kh.', 'type': 'consonant_punctuation'},
    chr(70671) + chr(70733): {'char': 'kh,', 'type': 'consonant_punctuation'},
    chr(70671) + chr(70734): {'char': 'kh..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70671) + chr(70735): {'char': 'kh...', 'type': 'consonant_punctuation'},
    chr(70671) + chr(70746): {'char': 'kh', 'type': 'consonant_punctuation'},  # double comma

    # g
    chr(70672) + chr(70731): {'char': 'g.', 'type': 'consonant_punctuation'},
    chr(70672) + chr(70732): {'char': 'g.', 'type': 'consonant_punctuation'},
    chr(70672) + chr(70733): {'char': 'g,', 'type': 'consonant_punctuation'},
    chr(70672) + chr(70734): {'char': 'g..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70672) + chr(70735): {'char': 'g...', 'type': 'consonant_punctuation'},
    chr(70672) + chr(70746): {'char': 'g', 'type': 'consonant_punctuation'},  # double comma

    # gh
    chr(70673) + chr(70731): {'char': 'gh.', 'type': 'consonant_punctuation'},
    chr(70673) + chr(70732): {'char': 'gh.', 'type': 'consonant_punctuation'},
    chr(70673) + chr(70733): {'char': 'gh,', 'type': 'consonant_punctuation'},
    chr(70673) + chr(70734): {'char': 'gh..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70673) + chr(70735): {'char': 'gh...', 'type': 'consonant_punctuation'},
    chr(70673) + chr(70746): {'char': 'gh', 'type': 'consonant_punctuation'},  # double comma

    # ng
    chr(70674) + chr(70731): {'char': 'ng.', 'type': 'consonant_punctuation'},
    chr(70674) + chr(70732): {'char': 'ng.', 'type': 'consonant_punctuation'},
    chr(70674) + chr(70733): {'char': 'ng,', 'type': 'consonant_punctuation'},
    chr(70674) + chr(70734): {'char': 'ng..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70674) + chr(70735): {'char': 'ng...', 'type': 'consonant_punctuation'},
    chr(70674) + chr(70746): {'char': 'ng', 'type': 'consonant_punctuation'},  # double comma

   

    # ngh
    chr(70675) + chr(70731): {'char': 'ngh.', 'type': 'consonant_punctuation'},
    chr(70675) + chr(70732): {'char': 'ngh.', 'type': 'consonant_punctuation'},
    chr(70675) + chr(70733): {'char': 'ngh,', 'type': 'consonant_punctuation'},
    chr(70675) + chr(70734): {'char': 'ngh..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70675) + chr(70735): {'char': 'ngh...', 'type': 'consonant_punctuation'},
    chr(70675) + chr(70746): {'char': 'ngh', 'type': 'consonant_punctuation'},  # double comma

    # ch
    chr(70676) + chr(70731): {'char': 'ch.', 'type': 'consonant_punctuation'},
    chr(70676) + chr(70732): {'char': 'ch.', 'type': 'consonant_punctuation'},
    chr(70676) + chr(70733): {'char': 'ch,', 'type': 'consonant_punctuation'},
    chr(70676) + chr(70734): {'char': 'ch..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70676) + chr(70735): {'char': 'ch...', 'type': 'consonant_punctuation'},
    chr(70676) + chr(70746): {'char': 'ch', 'type': 'consonant_punctuation'},  # double comma

    # cha
    chr(70677) + chr(70731): {'char': 'cha.', 'type': 'consonant_punctuation'},
    chr(70677) + chr(70732): {'char': 'cha.', 'type': 'consonant_punctuation'},
    chr(70677) + chr(70733): {'char': 'cha,', 'type': 'consonant_punctuation'},
    chr(70677) + chr(70734): {'char': 'cha..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70677) + chr(70735): {'char': 'cha...', 'type': 'consonant_punctuation'},
    chr(70677) + chr(70746): {'char': 'cha', 'type': 'consonant_punctuation'},  # double comma

    # j
    chr(70678) + chr(70731): {'char': 'j.', 'type': 'consonant_punctuation'},
    chr(70678) + chr(70732): {'char': 'j.', 'type': 'consonant_punctuation'},
    chr(70678) + chr(70733): {'char': 'j,', 'type': 'consonant_punctuation'},
    chr(70678) + chr(70734): {'char': 'j..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70678) + chr(70735): {'char': 'j...', 'type': 'consonant_punctuation'},
    chr(70678) + chr(70746): {'char': 'j', 'type': 'consonant_punctuation'},  # double comma

    # jh
    chr(70679) + chr(70731): {'char': 'jh.', 'type': 'consonant_punctuation'},
    chr(70679) + chr(70732): {'char': 'jh.', 'type': 'consonant_punctuation'},
    chr(70679) + chr(70733): {'char': 'jh,', 'type': 'consonant_punctuation'},
    chr(70679) + chr(70734): {'char': 'jh..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70679) + chr(70735): {'char': 'jh...', 'type': 'consonant_punctuation'},
    chr(70679) + chr(70746): {'char': 'jh', 'type': 'consonant_punctuation'},  # double comma

    # ny
    chr(70680) + chr(70731): {'char': 'ny.', 'type': 'consonant_punctuation'},
    chr(70680) + chr(70732): {'char': 'ny.', 'type': 'consonant_punctuation'},
    chr(70680) + chr(70733): {'char': 'ny,', 'type': 'consonant_punctuation'},
    chr(70680) + chr(70734): {'char': 'ny..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70680) + chr(70735): {'char': 'ny...', 'type': 'consonant_punctuation'},
    chr(70680) + chr(70746): {'char': 'ny', 'type': 'consonant_punctuation'},  # double comma

    # nyh
    chr(70681) + chr(70731): {'char': 'nyh.', 'type': 'consonant_punctuation'},
    chr(70681) + chr(70732): {'char': 'nyh.', 'type': 'consonant_punctuation'},
    chr(70681) + chr(70733): {'char': 'nyh,', 'type': 'consonant_punctuation'},
    chr(70681) + chr(70734): {'char': 'nyh..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70681) + chr(70735): {'char': 'nyh...', 'type': 'consonant_punctuation'},
    chr(70681) + chr(70746): {'char': 'nyh', 'type': 'consonant_punctuation'},  # double comma

    # tt
    chr(70682) + chr(70731): {'char': 'tt.', 'type': 'consonant_punctuation'},
    chr(70682) + chr(70732): {'char': 'tt.', 'type': 'consonant_punctuation'},
    chr(70682) + chr(70733): {'char': 'tt,', 'type': 'consonant_punctuation'},
    chr(70682) + chr(70734): {'char': 'tt..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70682) + chr(70735): {'char': 'tt...', 'type': 'consonant_punctuation'},
    chr(70682) + chr(70746): {'char': 'tt', 'type': 'consonant_punctuation'},  # double comma

    # tth
    chr(70683) + chr(70731): {'char': 'tth.', 'type': 'consonant_punctuation'},
    chr(70683) + chr(70732): {'char': 'tth.', 'type': 'consonant_punctuation'},
    chr(70683) + chr(70733): {'char': 'tth,', 'type': 'consonant_punctuation'},
    chr(70683) + chr(70734): {'char': 'tth..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70683) + chr(70735): {'char': 'tth...', 'type': 'consonant_punctuation'},
    chr(70683) + chr(70746): {'char': 'tth', 'type': 'consonant_punctuation'},  # double comma

    # dd
    chr(70684) + chr(70731): {'char': 'dd.', 'type': 'consonant_punctuation'},
    chr(70684) + chr(70732): {'char': 'dd.', 'type': 'consonant_punctuation'},
    chr(70684) + chr(70733): {'char': 'dd,', 'type': 'consonant_punctuation'},
    chr(70684) + chr(70734): {'char': 'dd..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70684) + chr(70735): {'char': 'dd...', 'type': 'consonant_punctuation'},
    chr(70684) + chr(70746): {'char': 'dd', 'type': 'consonant_punctuation'},  # double comma

    # ddh
    chr(70685) + chr(70731): {'char': 'ddh.', 'type': 'consonant_punctuation'},
    chr(70685) + chr(70732): {'char': 'ddh.', 'type': 'consonant_punctuation'},
    chr(70685) + chr(70733): {'char': 'ddh,', 'type': 'consonant_punctuation'},
    chr(70685) + chr(70734): {'char': 'ddh..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70685) + chr(70735): {'char': 'ddh...', 'type': 'consonant_punctuation'},
    chr(70685) + chr(70746): {'char': 'ddh', 'type': 'consonant_punctuation'},  # double comma

    # nn
    chr(70686) + chr(70731): {'char': 'nn.', 'type': 'consonant_punctuation'},
    chr(70686) + chr(70732): {'char': 'nn.', 'type': 'consonant_punctuation'},
    chr(70686) + chr(70733): {'char': 'nn,', 'type': 'consonant_punctuation'},
    chr(70686) + chr(70734): {'char': 'nn..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70686) + chr(70735): {'char': 'nn...', 'type': 'consonant_punctuation'},
    chr(70686) + chr(70746): {'char': 'nn', 'type': 'consonant_punctuation'},  # double comma

    # t
    chr(70687) + chr(70731): {'char': 't.', 'type': 'consonant_punctuation'},
    chr(70687) + chr(70732): {'char': 't.', 'type': 'consonant_punctuation'},
    chr(70687) + chr(70733): {'char': 't,', 'type': 'consonant_punctuation'},
    chr(70687) + chr(70734): {'char': 't..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70687) + chr(70735): {'char': 't...', 'type': 'consonant_punctuation'},
    chr(70687) + chr(70746): {'char': 't', 'type': 'consonant_punctuation'},  # double comma

    # th
    chr(70688) + chr(70731): {'char': 'th.', 'type': 'consonant_punctuation'},
    chr(70688) + chr(70732): {'char': 'th.', 'type': 'consonant_punctuation'},
    chr(70688) + chr(70733): {'char': 'th,', 'type': 'consonant_punctuation'},
    chr(70688) + chr(70734): {'char': 'th..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70688) + chr(70735): {'char': 'th...', 'type': 'consonant_punctuation'},
    chr(70688) + chr(70746): {'char': 'th', 'type': 'consonant_punctuation'},  # double comma

    # d
    chr(70689) + chr(70731): {'char': 'd.', 'type': 'consonant_punctuation'},
    chr(70689) + chr(70732): {'char': 'd.', 'type': 'consonant_punctuation'},
    chr(70689) + chr(70733): {'char': 'd,', 'type': 'consonant_punctuation'},
    chr(70689) + chr(70734): {'char': 'd..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70689) + chr(70735): {'char': 'd...', 'type': 'consonant_punctuation'},
    chr(70689) + chr(70746): {'char': 'd', 'type': 'consonant_punctuation'},  # double comma

    # dh
    chr(70690) + chr(70731): {'char': 'dh.', 'type': 'consonant_punctuation'},
    chr(70690) + chr(70732): {'char': 'dh.', 'type': 'consonant_punctuation'},
    chr(70690) + chr(70733): {'char': 'dh,', 'type': 'consonant_punctuation'},
    chr(70690) + chr(70734): {'char': 'dh..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70690) + chr(70735): {'char': 'dh...', 'type': 'consonant_punctuation'},
    chr(70690) + chr(70746): {'char': 'dh', 'type': 'consonant_punctuation'},  # double comma

    # n
    chr(70691) + chr(70731): {'char': 'n.', 'type': 'consonant_punctuation'},
    chr(70691) + chr(70732): {'char': 'n.', 'type': 'consonant_punctuation'},
    chr(70691) + chr(70733): {'char': 'n,', 'type': 'consonant_punctuation'},
    chr(70691) + chr(70734): {'char': 'n..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70691) + chr(70735): {'char': 'n...', 'type': 'consonant_punctuation'},
    chr(70691) + chr(70746): {'char': 'n', 'type': 'consonant_punctuation'},  # double comma

    # nh
    chr(70692) + chr(70731): {'char': 'nh.', 'type': 'consonant_punctuation'},
    chr(70692) + chr(70732): {'char': 'nh.', 'type': 'consonant_punctuation'},
    chr(70692) + chr(70733): {'char': 'nh,', 'type': 'consonant_punctuation'},
    chr(70692) + chr(70734): {'char': 'nh..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70692) + chr(70735): {'char': 'nh...', 'type': 'consonant_punctuation'},
    chr(70692) + chr(70746): {'char': 'nh', 'type': 'consonant_punctuation'},  # double comma

    # p
    chr(70693) + chr(70731): {'char': 'p.', 'type': 'consonant_punctuation'},
    chr(70693) + chr(70732): {'char': 'p.', 'type': 'consonant_punctuation'},
    chr(70693) + chr(70733): {'char': 'p,', 'type': 'consonant_punctuation'},
    chr(70693) + chr(70734): {'char': 'p..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70693) + chr(70735): {'char': 'p...', 'type': 'consonant_punctuation'},
    chr(70693) + chr(70746): {'char': 'p', 'type': 'consonant_punctuation'},  # double comma

    # ph
    chr(70694) + chr(70731): {'char': 'ph.', 'type': 'consonant_punctuation'},
    chr(70694) + chr(70732): {'char': 'ph.', 'type': 'consonant_punctuation'},
    chr(70694) + chr(70733): {'char': 'ph,', 'type': 'consonant_punctuation'},
    chr(70694) + chr(70734): {'char': 'ph..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70694) + chr(70735): {'char': 'ph...', 'type': 'consonant_punctuation'},
    chr(70694) + chr(70746): {'char': 'ph', 'type': 'consonant_punctuation'},  # double comma

    # b
    chr(70695) + chr(70731): {'char': 'b.', 'type': 'consonant_punctuation'},
    chr(70695) + chr(70732): {'char': 'b.', 'type': 'consonant_punctuation'},
    chr(70695) + chr(70733): {'char': 'b,', 'type': 'consonant_punctuation'},
    chr(70695) + chr(70734): {'char': 'b..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70695) + chr(70735): {'char': 'b...', 'type': 'consonant_punctuation'},
    chr(70695) + chr(70746): {'char': 'b', 'type': 'consonant_punctuation'},  # double comma

    # bh
    chr(70696) + chr(70731): {'char': 'bh.', 'type': 'consonant_punctuation'},
    chr(70696) + chr(70732): {'char': 'bh.', 'type': 'consonant_punctuation'},
    chr(70696) + chr(70733): {'char': 'bh,', 'type': 'consonant_punctuation'},
    chr(70696) + chr(70734): {'char': 'bh..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70696) + chr(70735): {'char': 'bh...', 'type': 'consonant_punctuation'},
    chr(70696) + chr(70746): {'char': 'bh', 'type': 'consonant_punctuation'},  # double comma

    # m
    chr(70697) + chr(70731): {'char': 'm.', 'type': 'consonant_punctuation'},
    chr(70697) + chr(70732): {'char': 'm.', 'type': 'consonant_punctuation'},
    chr(70697) + chr(70733): {'char': 'm,', 'type': 'consonant_punctuation'},
    chr(70697) + chr(70734): {'char': 'm..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70697) + chr(70735): {'char': 'm...', 'type': 'consonant_punctuation'},
    chr(70697) + chr(70746): {'char': 'm', 'type': 'consonant_punctuation'},  # double comma

    # mh
    chr(70698) + chr(70731): {'char': 'mh.', 'type': 'consonant_punctuation'},
    chr(70698) + chr(70732): {'char': 'mh.', 'type': 'consonant_punctuation'},
    chr(70698) + chr(70733): {'char': 'mh,', 'type': 'consonant_punctuation'},
    chr(70698) + chr(70734): {'char': 'mh..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70698) + chr(70735): {'char': 'mh...', 'type': 'consonant_punctuation'},
    chr(70698) + chr(70746): {'char': 'mh', 'type': 'consonant_punctuation'},  # double comma

    # y
    chr(70699) + chr(70731): {'char': 'y.', 'type': 'consonant_punctuation'},
    chr(70699) + chr(70732): {'char': 'y.', 'type': 'consonant_punctuation'},
    chr(70699) + chr(70733): {'char': 'y,', 'type': 'consonant_punctuation'},
    chr(70699) + chr(70734): {'char': 'y..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70699) + chr(70735): {'char': 'y...', 'type': 'consonant_punctuation'},
    chr(70699) + chr(70746): {'char': 'y', 'type': 'consonant_punctuation'},  # double comma

    # r
    chr(70700) + chr(70731): {'char': 'r.', 'type': 'consonant_punctuation'},
    chr(70700) + chr(70732): {'char': 'r.', 'type': 'consonant_punctuation'},
    chr(70700) + chr(70733): {'char': 'r,', 'type': 'consonant_punctuation'},
    chr(70700) + chr(70734): {'char': 'r..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70700) + chr(70735): {'char': 'r...', 'type': 'consonant_punctuation'},
    chr(70700) + chr(70746): {'char': 'r', 'type': 'consonant_punctuation'},  # double comma

    # rh
    chr(70701) + chr(70731): {'char': 'rh.', 'type': 'consonant_punctuation'},
    chr(70701) + chr(70732): {'char': 'rh.', 'type': 'consonant_punctuation'},
    chr(70701) + chr(70733): {'char': 'rh,', 'type': 'consonant_punctuation'},
    chr(70701) + chr(70734): {'char': 'rh..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70701) + chr(70735): {'char': 'rh...', 'type': 'consonant_punctuation'},
    chr(70701) + chr(70746): {'char': 'rh', 'type': 'consonant_punctuation'},  # double comma

    # l
    chr(70702) + chr(70731): {'char': 'l.', 'type': 'consonant_punctuation'},
    chr(70702) + chr(70732): {'char': 'l.', 'type': 'consonant_punctuation'},
    chr(70702) + chr(70733): {'char': 'l,', 'type': 'consonant_punctuation'},
    chr(70702) + chr(70734): {'char': 'l..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70702) + chr(70735): {'char': 'l...', 'type': 'consonant_punctuation'},
    chr(70702) + chr(70746): {'char': 'l', 'type': 'consonant_punctuation'},  # double comma

    # lh
    chr(70703) + chr(70731): {'char': 'lh.', 'type': 'consonant_punctuation'},
    chr(70703) + chr(70732): {'char': 'lh.', 'type': 'consonant_punctuation'},
    chr(70703) + chr(70733): {'char': 'lh,', 'type': 'consonant_punctuation'},
    chr(70703) + chr(70734): {'char': 'lh..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70703) + chr(70735): {'char': 'lh...', 'type': 'consonant_punctuation'},
    chr(70703) + chr(70746): {'char': 'lh', 'type': 'consonant_punctuation'},  # double comma

    # w
    chr(70704) + chr(70731): {'char': 'w.', 'type': 'consonant_punctuation'},
    chr(70704) + chr(70732): {'char': 'w.', 'type': 'consonant_punctuation'},
    chr(70704) + chr(70733): {'char': 'w,', 'type': 'consonant_punctuation'},
    chr(70704) + chr(70734): {'char': 'w..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70704) + chr(70735): {'char': 'w...', 'type': 'consonant_punctuation'},
    chr(70704) + chr(70746): {'char': 'w', 'type': 'consonant_punctuation'},  # double comma

    # sh
    chr(70705) + chr(70731): {'char': 'sh.', 'type': 'consonant_punctuation'},
    chr(70705) + chr(70732): {'char': 'sh.', 'type': 'consonant_punctuation'},
    chr(70705) + chr(70733): {'char': 'sh,', 'type': 'consonant_punctuation'},
    chr(70705) + chr(70734): {'char': 'sh..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70705) + chr(70735): {'char': 'sh...', 'type': 'consonant_punctuation'},
    chr(70705) + chr(70746): {'char': 'sh', 'type': 'consonant_punctuation'},  # double comma

    # ss
    chr(70706) + chr(70731): {'char': 'ss.', 'type': 'consonant_punctuation'},
    chr(70706) + chr(70732): {'char': 'ss.', 'type': 'consonant_punctuation'},
    chr(70706) + chr(70733): {'char': 'ss,', 'type': 'consonant_punctuation'},
    chr(70706) + chr(70734): {'char': 'ss..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70706) + chr(70735): {'char': 'ss...', 'type': 'consonant_punctuation'},
    chr(70706) + chr(70746): {'char': 'ss', 'type': 'consonant_punctuation'},  # double comma

    # s
    chr(70707) + chr(70731): {'char': 's.', 'type': 'consonant_punctuation'},
    chr(70707) + chr(70732): {'char': 's.', 'type': 'consonant_punctuation'},
    chr(70707) + chr(70733): {'char': 's,', 'type': 'consonant_punctuation'},
    chr(70707) + chr(70734): {'char': 's..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70707) + chr(70735): {'char': 's...', 'type': 'consonant_punctuation'},
    chr(70707) + chr(70746): {'char': 's', 'type': 'consonant_punctuation'},  # double comma

    # h
    chr(70708) + chr(70731): {'char': 'h.', 'type': 'consonant_punctuation'},
    chr(70708) + chr(70732): {'char': 'h.', 'type': 'consonant_punctuation'},
    chr(70708) + chr(70733): {'char': 'h,', 'type': 'consonant_punctuation'},
    chr(70708) + chr(70734): {'char': 'h..', 'type': 'consonant_punctuation'},  # gap filler
    chr(70708) + chr(70735): {'char': 'h...', 'type': 'consonant_punctuation'},
    chr(70708) + chr(70746): {'char': 'h', 'type': 'consonant_punctuation'},  # double comma

    # Vowels followed by punctuation
    # a
    chr(70656) + chr(70731): {'char': 'a.', 'type': 'independent_punctuation'},
    chr(70656) + chr(70732): {'char': 'a.', 'type': 'independent_punctuation'},
    chr(70656) + chr(70733): {'char': 'a,', 'type': 'independent_punctuation'},
    chr(70656) + chr(70734): {'char': 'a..', 'type': 'independent_punctuation'},  # gap filler
    chr(70656) + chr(70735): {'char': 'a...', 'type': 'independent_punctuation'},
    chr(70656) + chr(70746): {'char': 'a', 'type': 'independent_punctuation'},  # double comma

    # aa
    chr(70657) + chr(70731): {'char': 'aa.', 'type': 'independent_punctuation'},
    chr(70657) + chr(70732): {'char': 'aa.', 'type': 'independent_punctuation'},
    chr(70657) + chr(70733): {'char': 'aa,', 'type': 'independent_punctuation'},
    chr(70657) + chr(70734): {'char': 'aa..', 'type': 'independent_punctuation'},  # gap filler
    chr(70657) + chr(70735): {'char': 'aa...', 'type': 'independent_punctuation'},
    chr(70657) + chr(70746): {'char': 'aa', 'type': 'independent_punctuation'},  # double comma

    # i
    chr(70658) + chr(70731): {'char': 'i.', 'type': 'independent_punctuation'},
    chr(70658) + chr(70732): {'char': 'i.', 'type': 'independent_punctuation'},
    chr(70658) + chr(70733): {'char': 'i,', 'type': 'independent_punctuation'},
    chr(70658) + chr(70734): {'char': 'i..', 'type': 'independent_punctuation'},  # gap filler
    chr(70658) + chr(70735): {'char': 'i...', 'type': 'independent_punctuation'},
    chr(70658) + chr(70746): {'char': 'i', 'type': 'independent_punctuation'},  # double comma

    # ii
    chr(70659) + chr(70731): {'char': 'ii.', 'type': 'independent_punctuation'},
    chr(70659) + chr(70732): {'char': 'ii.', 'type': 'independent_punctuation'},
    chr(70659) + chr(70733): {'char': 'ii,', 'type': 'independent_punctuation'},
    chr(70659) + chr(70734): {'char': 'ii..', 'type': 'independent_punctuation'},  # gap filler
    chr(70659) + chr(70735): {'char': 'ii...', 'type': 'independent_punctuation'},
    chr(70659) + chr(70746): {'char': 'ii', 'type': 'independent_punctuation'},  # double comma

    # u
    chr(70660) + chr(70731): {'char': 'u.', 'type': 'independent_punctuation'},
    chr(70660) + chr(70732): {'char': 'u.', 'type': 'independent_punctuation'},
    chr(70660) + chr(70733): {'char': 'u,', 'type': 'independent_punctuation'},
    chr(70660) + chr(70734): {'char': 'u..', 'type': 'independent_punctuation'},  # gap filler
    chr(70660) + chr(70735): {'char': 'u...', 'type': 'independent_punctuation'},
    chr(70660) + chr(70746): {'char': 'u', 'type': 'independent_punctuation'},  # double comma

    # uu
    chr(70661) + chr(70731): {'char': 'uu.', 'type': 'independent_punctuation'},
    chr(70661) + chr(70732): {'char': 'uu.', 'type': 'independent_punctuation'},
    chr(70661) + chr(70733): {'char': 'uu,', 'type': 'independent_punctuation'},
    chr(70661) + chr(70734): {'char': 'uu..', 'type': 'independent_punctuation'},  # gap filler
    chr(70661) + chr(70735): {'char': 'uu...', 'type': 'independent_punctuation'},
    chr(70661) + chr(70746): {'char': 'uu', 'type': 'independent_punctuation'},  # double comma

    # r
    chr(70662) + chr(70731): {'char': 'r.', 'type': 'independent_punctuation'},
    chr(70662) + chr(70732): {'char': 'r.', 'type': 'independent_punctuation'},
    chr(70662) + chr(70733): {'char': 'r,', 'type': 'independent_punctuation'},
    chr(70662) + chr(70734): {'char': 'r..', 'type': 'independent_punctuation'},  # gap filler
    chr(70662) + chr(70735): {'char': 'r...', 'type': 'independent_punctuation'},
    chr(70662) + chr(70746): {'char': 'r', 'type': 'independent_punctuation'},  # double comma

    # rr
    chr(70663) + chr(70731): {'char': 'rr.', 'type': 'independent_punctuation'},
    chr(70663) + chr(70732): {'char': 'rr.', 'type': 'independent_punctuation'},
    chr(70663) + chr(70733): {'char': 'rr,', 'type': 'independent_punctuation'},
    chr(70663) + chr(70734): {'char': 'rr..', 'type': 'independent_punctuation'},  # gap filler
    chr(70663) + chr(70735): {'char': 'rr...', 'type': 'independent_punctuation'},
    chr(70663) + chr(70746): {'char': 'rr', 'type': 'independent_punctuation'},  # double comma

    # l
    chr(70664) + chr(70731): {'char': 'l.', 'type': 'independent_punctuation'},
    chr(70664) + chr(70732): {'char': 'l.', 'type': 'independent_punctuation'},
    chr(70664) + chr(70733): {'char': 'l,', 'type': 'independent_punctuation'},
    chr(70664) + chr(70734): {'char': 'l..', 'type': 'independent_punctuation'},  # gap filler
    chr(70664) + chr(70735): {'char': 'l...', 'type': 'independent_punctuation'},
    chr(70664) + chr(70746): {'char': 'l', 'type': 'independent_punctuation'},  # double comma

    # ll
    chr(70665) + chr(70731): {'char': 'll.', 'type': 'independent_punctuation'},
    chr(70665) + chr(70732): {'char': 'll.', 'type': 'independent_punctuation'},
    chr(70665) + chr(70733): {'char': 'll,', 'type': 'independent_punctuation'},
    chr(70665) + chr(70734): {'char': 'll..', 'type': 'independent_punctuation'},  # gap filler
    chr(70665) + chr(70735): {'char': 'll...', 'type': 'independent_punctuation'},
    chr(70665) + chr(70746): {'char': 'll', 'type': 'independent_punctuation'},  # double comma

    # e
    chr(70666) + chr(70731): {'char': 'e.', 'type': 'independent_punctuation'},
    chr(70666) + chr(70732): {'char': 'e.', 'type': 'independent_punctuation'},
    chr(70666) + chr(70733): {'char': 'e,', 'type': 'independent_punctuation'},
    chr(70666) + chr(70734): {'char': 'e..', 'type': 'independent_punctuation'},  # gap filler
    chr(70666) + chr(70735): {'char': 'e...', 'type': 'independent_punctuation'},
    chr(70666) + chr(70746): {'char': 'e', 'type': 'independent_punctuation'},  # double comma

    # ai
    chr(70667) + chr(70731): {'char': 'ai.', 'type': 'independent_punctuation'},
    chr(70667) + chr(70732): {'char': 'ai.', 'type': 'independent_punctuation'},
    chr(70667) + chr(70733): {'char': 'ai,', 'type': 'independent_punctuation'},
    chr(70667) + chr(70734): {'char': 'ai..', 'type': 'independent_punctuation'},  # gap filler
    chr(70667) + chr(70735): {'char': 'ai...', 'type': 'independent_punctuation'},
    chr(70667) + chr(70746): {'char': 'ai', 'type': 'independent_punctuation'},  # double comma

    # o
    chr(70668) + chr(70731): {'char': 'o.', 'type': 'independent_punctuation'},
    chr(70668) + chr(70732): {'char': 'o.', 'type': 'independent_punctuation'},
    chr(70668) + chr(70733): {'char': 'o,', 'type': 'independent_punctuation'},
    chr(70668) + chr(70734): {'char': 'o..', 'type': 'independent_punctuation'},  # gap filler
    chr(70668) + chr(70735): {'char': 'o...', 'type': 'independent_punctuation'},
    chr(70668) + chr(70746): {'char': 'o', 'type': 'independent_punctuation'},  # double comma

    # au
    chr(70669) + chr(70731): {'char': 'au.', 'type': 'independent_punctuation'},
    chr(70669) + chr(70732): {'char': 'au.', 'type': 'independent_punctuation'},
    chr(70669) + chr(70733): {'char': 'au,', 'type': 'independent_punctuation'},
    chr(70669) + chr(70734): {'char': 'au..', 'type': 'independent_punctuation'},  # gap filler
    chr(70669) + chr(70735): {'char': 'au...', 'type': 'independent_punctuation'},
    chr(70669) + chr(70746): {'char': 'au', 'type': 'independent_punctuation'},  # double comma



    #digits
    chr(70736): {'char': '0', 'type': 'digits'},
    chr(70737): {'char': '1', 'type': 'digits'},
    chr(70738): {'char': '2', 'type': 'digits'},
    chr(70739): {'char': '3', 'type': 'digits'},
    chr(70740): {'char': '4', 'type': 'digits'},
    chr(70741): {'char': '5', 'type': 'digits'},
    chr(70742): {'char': '6', 'type': 'digits'},
    chr(70743): {'char': '7', 'type': 'digits'},
    chr(70744): {'char': '8', 'type': 'digits'},
    chr(70745): {'char': '9', 'type': 'digits'},

    #symbols
    chr(70722): {'char': '', 'type': 'symbols'}, #virama
    chr(70723): {'char': 'n', 'type': 'symbols'},
    chr(70724): {'char': 'm', 'type': 'symbols'},
    chr(70725): {'char': 'h', 'type': 'symbols'},
    chr(70726): {'char': '', 'type': 'symbols'},
    chr(70727): {'char': '', 'type': 'symbols'},
    chr(70728): {'char': 'm', 'type': 'symbols'}, #final anusvara
    chr(70729): {'char': 'om', 'type': 'symbols'},
    chr(70730): {'char': 'n', 'type': 'symbols'}, # siddhi
    chr(70747): {'char': '', 'type': 'symbols'}, #placeholder mark
    chr(70748): {'char': '', 'type': 'symbols'}, #reserved
    chr(70749): {'char': '', 'type': 'symbols'}, #insertion sign
    chr(70750): {'char': '', 'type': 'symbols'}, #sandhi
    chr(70751): {'char': 'm', 'type': 'symbols'}, #vedic anusarva
    chr(70752): {'char': 't', 'type': 'symbols'}, #jihvamuliya
    chr(70753): {'char': 'n', 'type': 'symbols'}, #upadhmaniya

    #punctuation

    chr(70731): {'char': '.', 'type': 'punctuation'},
    chr(70732): {'char': '.', 'type': 'punctuation'},
    chr(70733): {'char': ',', 'type': 'punctuation'},
    chr(70734): {'char': '..', 'type': 'punctuation'}, #gap filler
    chr(70735): {'char': '...', 'type': 'punctuation'},
    chr(70746): {'char': '', 'type': 'punctuation'}, #double comma

    #space
    ' ': {'char': ' ', 'type': 'space'},


}
